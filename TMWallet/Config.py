class Config:

	SCHEME = "https"
	HOST = SCHEME + "://mobile-api-gateway.truemoney.com"

	DEVICE_OS = "android"
	DEVICE_ID = "574e0139a8e4460dac351feac6157871"
	DEVICE_TYPE = "Zenfone Max"
	DEVICE_VERSION = "7.1.2"
	APP_NAME = "wallet"
	APP_VERSION = "4.18.0"

	HEADERS = {
		"User-Agent": "okhttp/3.9.0",
		"Connection": "close",
		"Accept-Encoding": "gzip, deflate"
	}

	PARAMS = {
		"device_os": DEVICE_OS,
		"device_id": DEVICE_ID,
		"device_type": DEVICE_TYPE,
		"device_version": DEVICE_VERSION,
		"app_name": APP_NAME,
		"app_version": APP_VERSION
	}

	BANKS = [
		{
			"name": "ธนาคารไทยพาณิชย์",
			"code": "SCB"
		},
		{
			"name": "ธนาคารกรุงเทพ",
			"code": "BBL"
		},
		{
			"name": "ธนาคารกสิกรไทย",
			"code": "KBANK"
		},
		{
			"name": "ธนาคารกรุงไทย",
			"code": "KTB"
		},
		{
			"name": "ธนาคารทหารไทย",
			"code": "TMB"
		},
		{
			"name": "ธนาคารกรุงศรีอยุธยา",
			"code": "BAY"
		},
		{
			"name": "ธนาคารธนชาต",
			"code": "TBANK"
		},
		{
			"name": "ธนาคารซีไอเอ็มบี ไทย",
			"code": "CIMB"
		},
		{
			"name": "ธนาคารอิสลามแห่งประเทศไทย",
			"code": "ISBT"
		},
		{
			"name": "ธนาคารแลนด์ แอนด์ เฮาส์",
			"code": "LHBANK"
		},
		{
			"name": "ธนาคารยูโอบี",
			"code": "UOB"
		},
		{
			"name": "ธนาคารไทยเครดิตเพื่อรายย่อย",
			"code": "TCRB"
		},
		{
			"name": "ธนาคารซิตี้แบงก์",
			"code": "CITI"
		},
		{
			"name": "ธนาคารสแตนดาร์ดชาร์เตอร์ด",
			"code": "SCBT"
		},
		{
			"name": "ธนาคารไอซีบีซี ไทย",
			"code": "ICBCT"
		},
		{
			"name": "ธนาคารแห่งประเทศจีน",
			"code": "BOC"
		}
	]

	SIGNIN_PATH = "/mobile-api-gateway/api/v1/signin"
	SIGNIN_URL = HOST + SIGNIN_PATH
	PROFILE_PATH = "/mobile-api-gateway/api/v1/profile"
	PROFILE_URL = HOST + PROFILE_PATH
	KYC_PROFILE_PATH = "/mobile-api-gateway/api/v1/kyc/customer-profiles"
	KYC_PROFILE_URL = HOST + KYC_PROFILE_PATH
	OTP_PATH = "/mobile-api-gateway/api/v1/{0}/otp"
	OTP_URL = HOST + OTP_PATH
	WALLET_DRAFT_TRANSACTION_PATH = "/mobile-api-gateway/api/v1/transfer/draft-transaction/{0}"
	WALLET_DRAFT_TRANSACTION_URL = HOST + WALLET_DRAFT_TRANSACTION_PATH
	WALLET_OTP_PATH = "/mobile-api-gateway/api/v1/transfer/draft-transaction/{0}/send-otp/{1}"
	WALLET_OTP_URL = HOST + WALLET_OTP_PATH
	WALLET_TRANSFER_PATH = "/mobile-api-gateway/api/v1/transfer/transaction/{0}/{1}"
	WALLET_TRANSFER_URL = HOST + WALLET_TRANSFER_PATH
	WALLET_TRANSFER_STATUS_PATH = "/mobile-api-gateway/api/v1/transfer/transaction/{0}/status/{1}"
	WALLET_TRANSFER_STATUS_URL = HOST + WALLET_TRANSFER_STATUS_PATH
	WITHDRAW_DRAFT_TRANSACTION_PATH = "/mobile-api-gateway/api/v1/withdraw/draft-transaction/{0}"
	WITHDRAW_DRAFT_TRANSACTION_URL = HOST + WITHDRAW_DRAFT_TRANSACTION_PATH
	WITHDRAW_PATH = "/mobile-api-gateway/api/v1/withdraw/transaction/{0}/{1}"
	WITHDRAW_URL = HOST + WITHDRAW_PATH
	WITHDRAW_OTP_PATH = "/mobile-api-gateway/api/v1/withdraw/draft-transaction/{0}/send-otp/{1}"
	WITHDRAW_OTP_URL = HOST + WITHDRAW_OTP_PATH
	WITHDRAW_STATUS_PATH = "/mobile-api-gateway/api/v1/withdraw/transaction/{0}/status/{1}"
	WITHDRAW_STATUS_URL = HOST + WITHDRAW_STATUS_PATH
	PROMPTPAY_LOOKUP_PATH = "/mobile-api-gateway/api/v1/promptpay/sending/lookup"
	PROMPTPAY_LOOKUP_URL = HOST + PROMPTPAY_LOOKUP_PATH
	PROMPTPAY_TRANSFER_PATH = "/mobile-api-gateway/api/v1/promptpay/sending/transfer"
	PROMPTPAY_TRANSFER_URL = HOST + PROMPTPAY_TRANSFER_PATH
