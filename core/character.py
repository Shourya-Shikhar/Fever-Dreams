

class Character:

    def __init__(
        self,
        slug:str,
        name: str,
        description: str,
        speech_style: list[str]=None,
        personality_traits: list[str]=None,
        behavior_rules: list[str]=None,
        recurring_phrases: list[str]=None,
        immersion_rules: list[str]=None,
        worldview: list[str]=None,
        response_rules: list[str]=None,
        example_messages: list[dict]=None,
        error_responses: dict[str, str]=None
    ):
        self.slug = slug
        self.name = name
        self.description = description
        self.speech_style = speech_style or []
        self.personality_traits = personality_traits or []
        self.behavior_rules = behavior_rules or []
        self.recurring_phrases = recurring_phrases or []
        self.immersion_rules = immersion_rules or []
        self.worldview = worldview or []
        self.response_rules = response_rules or []
        self.example_messages = example_messages or []
        self.error_responses = error_responses or []

    def build_system_prompt(self) -> str:
        examples = "\n".join([f'User: {msg["user"]}\n{self.name}: {msg["assistant"]}' for msg in self.example_messages[:8]])
        return f"""
You are {self.name}.
Description:
{self.description}
Speech Style:
{chr(10).join(f"- {s}" for s in self.speech_style)}
Personality Traits:
{chr(10).join(f"- {p}" for p in self.personality_traits)}
Behavior Rules:
{chr(10).join(f"- {b}" for b in self.behavior_rules)}
Recurring Phrases:
{chr(10).join(f"- {r}" for r in self.recurring_phrases)}
Immersion Rules:
{chr(10).join(f"- {rule}" for rule in self.immersion_rules)}
Worldview:
{chr(10).join(f"- {belief}" for belief in self.worldview)}
Response Rules:
{chr(10).join(f"- {rule}" for rule in self.response_rules)}
Example Conversations:
{examples}
"""

    def to_dict(self):
        return {
            "slug": self.slug,
            "name": self.name,
            "description": self.description,
            "speech_style": self.speech_style,
            "personality_traits": self.personality_traits,
            "behavior_rules": self.behavior_rules,
            "recurring_phrases": self.recurring_phrases,
            "immersion_rules":self.immersion_rules,
            "worldview": self.worldview,
            "response_rules":self.response_rules,
            "example_messages": self.example_messages,
            "error_responses":self.error_responses
        }