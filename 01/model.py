class SomeModel:
    def predict(self, message: str) -> float:
        summa = (
            sum([ord(char) for char in message]) * len(message) ** 2 / 1114111 * 0.25
        )
        return 0.999999999 if summa >= 1 else summa


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    x = model.predict(message)
    match x:
        case x if x < bad_thresholds:
            return "неуд"
        case x if x > good_thresholds:
            return "отл"
        case x:
            return "норм"


model = SomeModel()
assert predict_message_mood("Чапаев и пустота", model) == "отл"
assert predict_message_mood("Вулкан", model) == "неуд"
