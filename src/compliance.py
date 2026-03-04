def classify_message(message: str) -> str:
    """
    Free compliance guardrail classifier.
    Simulates an AI classification layer.
    """

    message_lower = message.lower()

    banned_phrases = [
        "guaranteed",
        "assured returns",
        "risk-free",
        "double your money"
    ]

    advisory_phrases = [
        "buy this stock",
        "invest now",
        "strong buy",
        "high return investment"
    ]

    for phrase in banned_phrases:
        if phrase in message_lower:
            return "Rejected"

    for phrase in advisory_phrases:
        if phrase in message_lower:
            return "Requires Review"

    return "Approved"