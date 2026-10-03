# CodeAlpha_BasicChatbot

A simple rule-based chatbot built in Python as part of the CodeAlpha Python Programming internship (Task 3).

## About

The chatbot replies to a set of predefined user inputs (greetings, small talk, goodbyes) with fixed responses. Anything outside its known inputs gets a generic fallback reply.

## Features

- Recognizes common greetings (hello, hi, hey)
- Responds to small talk like "how are you"
- Handles thanks and goodbyes, ending the conversation on "bye"
- Fallback response for anything it doesn't recognize

## Requirements

- Python 3.6+

No external dependencies — uses only the standard library.

## Usage

Run the script:

```bash
python chatbot.py
```

Type a message and the bot will reply. Type `bye` to end the conversation.

## Example

```
=== Simple Chatbot ===
Type 'bye' to end the conversation.

You: hello
Bot: Hi! How can I help you today?
You: how are you
Bot: I'm fine, thanks! How about you?
You: bye
Bot: Goodbye! Have a great day!
```

## Concepts Used

`if-elif`, functions, loops, input/output.

## License

Free to use, modify, and distribute.
