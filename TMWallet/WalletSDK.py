from .Config import Config
from urllib.parse import urlencode
import hashlib
import requests

class Wallet:

	isLogged = False

	fullname = None
	name = None
	mobileNumber = None
	email = None
	tmnId = None
	thaiId = None
	ewalletId = None

	def __init__(self, email, password):
		password = hashlib.sha1(("%s%s" % (email, password)).encode("utf-8")).hexdigest()

		jsonData = {
			"username": email,
			"password": password,
			"type": "email"
		}
		jsonResp = requests.post(Config.SIGNIN_URL, headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()

		if jsonResp["code"] == "20000":
			self.accessToken = jsonResp["data"]["accessToken"]
			self.fullname = jsonResp["data"]["fullname"]
			self.name = jsonResp["data"]["title"] + " " + jsonResp["data"]["fullname"]
			self.mobileNumber = jsonResp["data"]["mobileNumber"]
			self.email = jsonResp["data"]["email"]
			self.currentBalance = jsonResp["data"]["currentBalance"]
			self.tmnId = jsonResp["data"]["tmnId"]
			self.thaiId = jsonResp["data"]["thaiId"]

			headers = Config.HEADERS
			headers["Authorization"] = "Bearer " + self.accessToken
			self.ewalletId = requests.get(Config.KYC_PROFILE_URL + "/" + self.mobileNumber, headers=headers).json()["data"]["ewallet_id"]
			self.isLogged = True
		else:
			raise Exception("Cannot signin")

	def updateCurrentBalance(self):
		self.currentBalance = requests.get(Config.PROFILE_URL + "/" + self.accessToken, headers=Config.HEADERS, params=Config.PARAMS).json()["data"]["currentBalance"]
		return self.currentBalance

	def otp(self):
		return requests.get(Config.OTP_URL.format(self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]

	def promptpayLookup(self, receiverPromptpayAccountId, amount):
		params = {
			"access_token": self.accessToken
		}
		jsonData = {
			"amount": amount,
			"inputMethod": "keyIn",
			"receiverPromptpayAccountId": receiverPromptpayAccountId,
			"senderTmnProfile": {
				"ewalletId": self.ewalletId,
				"fullName": self.fullname,
				"mobileNumber": self.mobileNumber,
				"thaiId": self.thaiId,
				"tmnId": self.tmnId
			}
		}
		return requests.post(Config.PROMPTPAY_LOOKUP_URL, headers=Config.HEADERS, params=params, json=jsonData).json()["data"]

	def promptpayTransfer(self, draftTransactionId, otpString, otpRefCode):
		params = {
			"access_token": self.accessToken
		}
		jsonData = {
			"channelId": "46",
			"draftTransactionId": draftTransactionId,
			"inputMethod": "keyIn",
			"otpRefCode": otpRefCode,
			"otpString": otpString,
			"senderMobileNumber": self.mobileNumber,
			"tmnId": self.tmnId
		}
		return requests.post(Config.PROMPTPAY_TRANSFER_URL, headers=Config.HEADERS, params=params, json=jsonData).json()["data"]

	def walletDraftTransaction(self, amount, mobileNumber):
		jsonData = {
			"amount": amount,
			"mobileNumber": mobileNumber
		}
		return requests.post(Config.WALLET_DRAFT_TRANSACTION_URL.format(self.accessToken), headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()["data"]

	def walletOtp(self, draftTransactionId, personalMessage=""):
		jsonData = {
			"personalMessage": personalMessage
		}
		return requests.put(Config.WALLET_OTP_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()["data"]

	def walletTransfer(self, draftTransactionId, otpString, otpRefCode):
		jsonData = {
			"mobileNumber": self.mobileNumber,
			"otpString": otpString,
			"otpRefCode": otpRefCode
		}
		return requests.post(Config.WALLET_TRANSFER_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()["data"]

	def walletTransferStatus(self, draftTransactionId):
		return requests.get(Config.WALLET_TRANSFER_STATUS_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]

	def walletTransferSummery(self, draftTransactionId):
		return requests.get(Config.WALLET_TRANSFER_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]

	def withdrawDraftTransaction(self, bankName, bankAccount, amount):
		jsonData = {
			"amount": amount,
			"bankAccount": bankAccount,
			"bankName": bankName
		}
		return requests.post(Config.WITHDRAW_DRAFT_TRANSACTION_URL.format(self.accessToken), headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()["data"]

	def withdrawOtp(self, draftTransactionId):
		return requests.put(Config.WITHDRAW_OTP_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]

	def withdraw(self, draftTransactionId, otpString, otpRefCode, password):
		jsonData = {
			"mobileNumber": self.mobileNumber,
			"otpRefCode": otpRefCode,
			"otpString": otpString,
			"password": password
		}
		return requests.post(Config.WITHDRAW_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()["data"]

	def withdrawStatus(self, draftTransactionId):
		return requests.get(Config.WITHDRAW_STATUS_URL.format(draftTransactionId, self.accessToken), headers=headers, params=Config.PARAMS).json()["data"]

	def withdrawInfo(self, draftTransactionId):
		return requests.get(Config.WITHDRAW_PATH.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]
