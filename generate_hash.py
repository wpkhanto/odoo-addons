from passlib.context import CryptContext

# สร้าง context สำหรับการแฮชรหัสผ่าน
pwd_context = CryptContext(schemes=["pbkdf2_sha512"], deprecated="auto")

# รหัสผ่านที่ต้องการแฮช
password = "admin"

# แฮชรหัสผ่าน
hashed_password = pwd_context.hash(password)

print(hashed_password)
