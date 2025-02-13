class ForFixtures():
    USERVALUE = {"name": "Алексей","email": "nacharkin16@gmail.com","password": "nacharkin321"}

class TestValues():
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]}
    FLUORESTENTIC_BUN = "Метеоритный флюоресцентный бургер"
    UNCORRECTED_INGREDIENT = {"ingredients": ["61c0c5a71d1f82001bdaaa68"]}
    MESSAGE_UFILLED_ID_INGREDIENTS = 'Ingredient ids must be provided'
    UNCORRECTED_INGREDIENT_ID_MESSAGE = "One or more ids provided are incorrect"
    USER_EXIST_MESSAGE = "User already exists"
    VALUES_IN_REQUIRED_FIELDS_EMPTY = 'Email, password and name are required fields'
    VALUES_FOR_AUTHORIZATION = {"email": "nacharkin16@gmail.com","password": "nacharkin321"}
    MESSAGE_UNCORRECT_VALUES_FOR_AUTHORIZATION = "email or password are incorrect"
    MESSAGE_SHOULD_AUTHORIZATION = "You should be authorised"