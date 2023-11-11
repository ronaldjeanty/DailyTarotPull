import random

# Define a list of tarot cards
tarot_cards = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",

    "Ace of Wands",
    "Two of Wands",
    "Three of Wands",
    "Four of Wands",
    "Five of Wands",
    "Six of Wands",
    "Seven of Wands",
    "Eight of Wands",
    "Nine of Wands",
    "Ten of Wands",
    "Page of Wands",
    "Knight of Wands",
    "Queen of Wands",
    "King of Wands",

    "Ace of Cups",
    "Two of Cups",
    "Three of Cups",
    "Four of Cups",
    "Five of Cups",
    "Six of Cups",
    "Seven of Cups",
    "Eight of Cups",
    "Nine of Cups",
    "Ten of Cups",
    "Page of Cups",
    "Knight of Cups",
    "Queen of Cups",
    "King of Cups",

    "Ace of Swords",
    "Two of Swords",
    "Three of Swords",
    "Four of Swords",
    "Five of Swords",
    "Six of Swords",
    "Seven of Swords",
    "Eight of Swords",
    "Nine of Swords",
    "Ten of Swords",
    "Page of Swords",
    "Knight of Swords",
    "Queen of Swords",
    "King of Swords",

    "Ace of Pentacles",
    "Two of Pentacles",
    "Three of Pentacles",
    "Four of Pentacles",
    "Five of Pentacles",
    "Six of Pentacles",
    "Seven of Pentacles",
    "Eight of Pentacles",
    "Nine of Pentacles",
    "Ten of Pentacles",
    "Page of Pentacles",
    "Knight of Pentacles",
    "Queen of Pentacles",
    "King of Pentacles",






    # Add more cards as needed
]

# A dictionary mapping each card to a brief description
card_meanings = {
    "The Fool": "New beginnings, Spontaneity, Innocence.",
    "The Magician": "Manifestation, Power, Resourcefulness.",
    "The High Priestess": "Intuition, Unconscious knowledge, Mystery.",
    "The Empress": "Nurturing, Fertility, Abundance.",
    "The Emperor": "Authority, Structure, Leadership.",
    "The Hierophant": "Tradition, Spiritual guidance, Conformity.",
    "The Lovers": "Harmony, Relationships, Choices.",
    "The Chariot": "Control, Determination, Victory.",
    "Strength": "Inner strength, Courage, Compassion.",
    "The Hermit": "Solitude, Introspection, Guidance.",

    "Ace of Wands": "New beginnings, Inspiration, Potential.",
    "Two of Wands": "Planning, Decisions, Progress.",
    "Three of Wands": "Expansion, Foresight, Leadership.",
    "Four of Wands": "Celebration, Achievement, Harmony.",
    "Five of Wands": "Conflict, Competition, Challenges.",
    "Six of Wands": "Victory, Recognition, Success.",
    "Seven of Wands": "Defensiveness, Perseverance, Standing tall.",
    "Eight of Wands": "Swiftness, Progress, Communication.",
    "Nine of Wands": "Resilience, Determination, Strength.",
    "Ten of Wands": "Burden, Responsibility, Hard work.",
    "Page of Wands": "Exploration, Enthusiasm, New opportunities.",
    "Knight of Wands": "Action, Adventure, Impulsiveness.",
    "Queen of Wands": "Confidence, Leadership, Charisma.",
    "King of Wands": "Authority, Vision, Inspiration.",

    "Ace of Cups": "Spirituality, Intuition, New relationships.",
    "Two of Cups": "Unity, Partnership, Connection.",
    "Three of Cups": "Celebration, Friendship, Happiness.",
    "Four of Cups": "Apathy, Contemplation, Disconnection.",
    "Five of Cups": "Loss, Disappointment, Grief",
    "Six of Cups": "Memories, Healing, Restoration.",
    "Seven of Cups": "Daydreaming, Choices, Purpose Finding.",
    "Eight of Cups": "Leave it behind, Disillusion, Walk Away.",
    "Nine of Cups": "Luxury, Satisfaction, Emotional Stability.",
    "Ten of Cups": "Inner Happiness, Fulfillment, Dreams Come True.",
    "Page of Cups": "Happy Surprise, Dreamer, Sensitive. ",
    "Knight of Cups": "Romantic, Idealistic, Follow your Heart.",
    "Queen of Cups": "Compassion, Calm, Comfort.",
    "King of Cups": "Emotional Control, Balance, Heart and Mind.",

    "Ace of Swords": "Clarity, Truth, Breakthrough.",
    "Two of Swords": "Decision-making, Balance, Duality.",
    "Three of Swords": "Heartbreak, Sorrow, Emotional pain.",
    "Four of Swords": "Rest, Restoration, Contemplation.",
    "Five of Swords": "Ambitious, Winning, Sneakiness.",
    "Six of Swords": "Transition, Leaving Behind, Moving On.",
    "Seven of Swords": "Deception, Trickery, Strategy.",
    "Eight of Swords": "Imprisonment, Entrapment, Self-Victimization.",
    "Nine of Swords": "Anxiety, Hopelessness, Trauma.",
    "Ten of Swords": "Failure, Collapse, Defeat",
    "Page of Swords": "Curiosity, Restlessness, Mental Energy.",
    "Knight of Swords": "Action, Impulsiveness, Defending Beliefs.",
    "Queen of Swords": "Complexity, Perceptive, Clear Mindedness.",
    "King of Swords": "Head over heart, Truth, Discipline.",

    "Ace of Pentacles": "Material abundance, Prosperity, Security.",
    "Two of Pentacles": "Balance, Flexibility, Adaptability.",
    "Three of Pentacles": "Teamwork, Collaboration, Skill.",
    "Four of Pentacles": "Conservation, Security, Frugality.",
    "Five of Pentacles": "Low Resources, Insecurity, Need.",
    "Six of Pentacles": "Charity, Generosity, Sharing.",
    "Seven of Pentacles": "Hard Word, Perseverance, Diligence.",
    "Eight of Pentacles": "Passion, Inspiration, High Standard.",
    "Nine of Pentacles": "Fruits of labor, Reckless Spreading, Rewards.",
    "Ten of Pentacles": "Legacy, Inheritance, Culmination.",
    "Page of Pentacles": "Ambition, Desire, New Venture.",
    "Knight of Pentacles": "Efficiency, Hard work, Responsibility.",
    "Queen of Pentacles": "Practicality, Comfort, Security.",
    "King of Pentacles": "Abundance, Generosity, Abundance.",

    # Add more meanings as needed
}


def pull_tarot_card(previous_card=None):
    # Ensure the new card is different from the previous one
    new_card = previous_card
    while new_card == previous_card:
        new_card = random.choice(tarot_cards)

    return new_card


def get_card_meaning(card):
    return card_meanings.get(card, "Meaning not available.")


# Main program
previous_card = None
for _ in range(2):  # You can change the number of pulls as needed
    current_card = pull_tarot_card(previous_card)
    card_meaning = get_card_meaning(current_card)

    print(f"You pulled the {current_card} card.")
    print(f"Meaning: {card_meaning}\n")

    previous_card = current_card

