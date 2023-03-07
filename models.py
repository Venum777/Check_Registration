class User:

    email: str
    old: int
    password: str
    password2: int
    
    @staticmethod
    def create(
        email: str,
        old: int,
        password: str,
        password2: int,
        address: str
    )-> 'User':
        user: 'User' = User()
        user.old = old
        user.email = email
        user.password = password
        user.password2 = password2
        user.address = address
        user.validation()
        return user
    
    def validation(self) -> bool:
        User.validation_email(self.email)
        User.validation_password(self.password)
        User.validation_address(self.address)
        User.validation_old(self.old)
        
    @staticmethod
    def validation_email(email: str):
        high_lvl_domain_pattern: tuple = (
            'net', 'com', 'kz', 'ru',
            'org', 'eu', 'cc', 'ua'
        )
        email_parts: list[str] = email.split('@')
        email_parts_by_point: list[str] = email.split('.')

        if (
            len(email_parts) != 2
        ) or (
            len(email_parts[0]) <= 2
        ) or (
            len(email_parts) != 2
        ) or (
            not email_parts_by_point[1] in high_lvl_domain_pattern
        ):
            raise ValueError(
                "Не верынй Email!"
            )
    
    @staticmethod
    def validation_old(old: int):
        if old < 16 or old > 120:
            raise ValueError(
                "Не коректный возраст!"
            )
    
    @staticmethod
    def validation_password(password: str, password2: str):
        if (
            len(password) < 6 
        ) or (
            len(password) > 20
        ) or (
            password != password2
        ):
            raise ValueError(
                "Не коректный пароль!"
            )
            
    @staticmethod
    def validation_address(address: str):
        address_parts: list[str] = address.split(',')
        cityes: list[str] = [
            "Караганда",
        ]

        if (
            len(address_parts) != 6
        ) or (
            address_parts[0] != "Казахстан"
        ) or (
            address_parts[1] not in cityes
        ):
            raise ValueError(
                "Не коректный Адресс!"
            )
        


a = User.create(
    email="root@gmail.com",
    old=13,
    password="qwerty",
    password2="qwerty"
)