"""
Message Generator Module
Generates random messages for Discord bot automation
"""

import random
from datetime import datetime

class MessageGenerator:
    def __init__(self):
        self.greetings = [
            "Hey there!", "Hello!", "Hi everyone!", "Good day!", "Greetings!",
            "What's up?", "Howdy!", "Hey!", "Yo!", "Hiya!"
        ]
        
        self.topics = [
            "I just discovered something amazing!",
            "Check this out, it's incredible!",
            "Has anyone tried this yet?",
            "This is really interesting!",
            "I wanted to share this with you all.",
            "You won't believe what I found!",
            "This is worth checking out!",
            "I think you'll find this useful.",
            "Something cool I came across today.",
            "This caught my attention!"
        ]
        
        self.questions = [
            "What do you think about this?",
            "Any thoughts on this?",
            "Has anyone else experienced this?",
            "Would love to hear your opinions!",
            "What's your take on this?",
            "Anyone want to discuss this?",
            "Curious what you all think!",
            "Looking forward to your feedback!",
            "What are your thoughts?",
            "Does this make sense to you?"
        ]
        
        self.casual_messages = [
            "Hope everyone's having a great day! 😊",
            "Just wanted to say hi to everyone!",
            "Looking forward to chatting with you all!",
            "Happy to be part of this community!",
            "Great vibes here today! ✨",
            "Thanks for being awesome, everyone!",
            "Excited to be here!",
            "You all are amazing! 💪",
            "Such a great community we have here!",
            "Loving the energy in here! 🔥"
        ]
        
        self.emojis = ["😊", "👍", "🔥", "✨", "💯", "🎉", "👏", "💪", "🌟", "❤️", "🚀", "⭐"]
        
        self.links_examples = [
            "youtube.com/watch?v=example",
            "github.com/awesome-project",
            "medium.com/article-title",
            "twitter.com/status/123456"
        ]
        
        self.templates = [
            "{greeting} {topic}",
            "{topic} {question}",
            "{casual}",
            "{greeting} {casual}",
            "{topic} {emoji}",
            "{greeting} {topic} {question}",
            "{casual} {emoji}",
        ]
    
    def generate_single_message(self):
        """Generate a single random message"""
        template = random.choice(self.templates)
        
        message = template.format(
            greeting=random.choice(self.greetings),
            topic=random.choice(self.topics),
            question=random.choice(self.questions),
            casual=random.choice(self.casual_messages),
            emoji=random.choice(self.emojis)
        )
        
        # Randomly add extra emoji
        if random.random() > 0.7:
            message += " " + random.choice(self.emojis)
        
        return message
    
    def generate_messages(self, count=20):
        """Generate multiple unique messages"""
        messages = []
        for _ in range(count):
            msg = self.generate_single_message()
            # Ensure uniqueness
            while msg in messages:
                msg = self.generate_single_message()
            messages.append(msg)
        
        return messages
    
    def generate_promotional_message(self, product_name="", link=""):
        """Generate a promotional message"""
        promos = [
            f"🔥 Check out {product_name}! It's amazing! {link}",
            f"🌟 Just discovered {product_name} and I'm loving it! {link}",
            f"💯 Highly recommend {product_name} to everyone! {link}",
            f"✨ {product_name} is a game changer! Check it out: {link}",
            f"🚀 You need to see this: {product_name} {link}"
        ]
        return random.choice(promos)
    
    def generate_conversational_message(self):
        """Generate a natural conversational message"""
        conversations = [
            "Been thinking about this for a while now...",
            "Quick question for everyone here",
            "Does anyone know more about this?",
            "I've been working on something interesting",
            "Just wanted to share my experience with this",
            "Anyone else noticed this trend?",
            "This is fascinating, let me know what you think",
            "I found this really helpful",
            "Sharing this because it helped me a lot",
            "You might find this useful too"
        ]
        return random.choice(conversations)
    
    def generate_timestamped_message(self):
        """Generate a message with timestamp"""
        base_msg = self.generate_single_message()
        timestamp = datetime.now().strftime("%H:%M")
        return f"[{timestamp}] {base_msg}"
    
    def generate_custom_template(self, template_string, variables):
        """Generate message from custom template
        
        Args:
            template_string: String with {variable} placeholders
            variables: Dict of variable values
        """
        try:
            return template_string.format(**variables)
        except KeyError as e:
            return f"Error: Missing variable {e}"


# Example usage
if __name__ == "__main__":
    generator = MessageGenerator()
    
    print("=== Generated Messages ===\n")
    messages = generator.generate_messages(10)
    for i, msg in enumerate(messages, 1):
        print(f"{i}. {msg}")
    
    print("\n=== Promotional Message ===")
    print(generator.generate_promotional_message("Amazing Product", "https://example.com"))
    
    print("\n=== Conversational Message ===")
    print(generator.generate_conversational_message())
    
    print("\n=== Timestamped Message ===")
    print(generator.generate_timestamped_message())
