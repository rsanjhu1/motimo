from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Predefined Q&A for Motimo
responses = {
    "how to stay motivated": (
        "Staying motivated can be tough but breaking things down helps.\n"
        "1. Break your goal into small, manageable tasks.\n"
        "2. Celebrate each small win to keep motivation high.\n"
        "3. Remind yourself why you started."
    ),
    "how to overcome failure": (
        "Failure is just feedback guiding you to improve.\n"
        "1. Reflect on what you learned.\n"
        "2. Adjust your approach.\n"
        "3. Keep moving forward with new insights."
    ),
    "how to build confidence": (
        "Confidence grows from small wins and self-belief.\n"
        "1. Set small achievable goals.\n"
        "2. Acknowledge your progress daily.\n"
        "3. Practice positive self-talk."
    ),
    "how to manage stress": (
        "Stress affects us all but can be managed with simple techniques.\n"
        "1. Practice deep breathing exercises.\n"
        "2. Take short breaks during work.\n"
        "3. Focus on what’s in your control."
    ),
    "how to set goals": (
        "Clear goals guide your actions effectively.\n"
        "1. Use the SMART method: Specific, Measurable, Achievable, Relevant, Time-bound.\n"
        "2. Write down your goals.\n"
        "3. Review and adjust regularly."
    ),
    "how to focus better": (
        "Focus improves when distractions are minimized.\n"
        "1. Remove all distractions from your workspace.\n"
        "2. Use a timer for focused work sessions (e.g., Pomodoro).\n"
        "3. Take regular short breaks."
    ),
    "how to wake up early": (
        "Waking up early requires good sleep habits.\n"
        "1. Go to bed early and keep a consistent sleep schedule.\n"
        "2. Avoid screens before bedtime.\n"
        "3. Place your alarm clock away from your bed."
    ),
    "how to beat procrastination": (
        "Procrastination can be tackled with small actions.\n"
        "1. Start with just 5 minutes of work.\n"
        "2. Break tasks into smaller chunks.\n"
        "3. Reward yourself after completing tasks."
    ),
    "how to deal with negative people": (
        "Protect your mental space from negativity.\n"
        "1. Set clear boundaries.\n"
        "2. Limit your exposure when possible.\n"
        "3. Focus on positive relationships."
    ),
    "how to develop discipline": (
        "Discipline builds success habits.\n"
        "1. Create a daily routine.\n"
        "2. Stick to your plan even when motivation fades.\n"
        "3. Track your progress and adjust."
    ),
    "how to improve communication": (
        "Good communication strengthens relationships.\n"
        "1. Listen actively.\n"
        "2. Speak clearly and calmly.\n"
        "3. Ask questions to clarify."
    ),
    "how to build good habits": (
        "Habits shape your daily life.\n"
        "1. Start small and be consistent.\n"
        "2. Link new habits to existing routines.\n"
        "3. Reward yourself for sticking to them."
    ),
    "how to stay positive": (
        "Positive thinking improves wellbeing.\n"
        "1. Practice gratitude daily.\n"
        "2. Challenge negative thoughts.\n"
        "3. Surround yourself with supportive people."
    ),
    "how to manage time": (
        "Good time management boosts productivity.\n"
        "1. Prioritize tasks.\n"
        "2. Use time-blocking techniques.\n"
        "3. Avoid multitasking."
    ),
    "how to handle criticism": (
        "Constructive criticism helps you grow.\n"
        "1. Listen without interrupting.\n"
        "2. Separate feelings from facts.\n"
        "3. Use feedback to improve."
    ),
    "how to stay calm under pressure": (
        "Staying calm helps clear thinking.\n"
        "1. Take deep breaths.\n"
        "2. Focus on the present moment.\n"
        "3. Break problems into smaller steps."
    ),
    "how to increase creativity": (
        "Creativity comes from new experiences.\n"
        "1. Change your environment.\n"
        "2. Take breaks and relax.\n"
        "3. Try brainstorming without judgment."
    ),
    "how to be more productive": (
        "Productivity is about working smarter.\n"
        "1. Plan your day the night before.\n"
        "2. Use focused work sessions.\n"
        "3. Limit distractions."
    ),
    "how to improve self-esteem": (
        "Self-esteem grows with self-care.\n"
        "1. Practice positive affirmations.\n"
        "2. Set realistic expectations.\n"
        "3. Celebrate your achievements."
    ),
    "how to maintain work-life balance": (
        "Balance keeps you healthy and happy.\n"
        "1. Set clear boundaries.\n"
        "2. Schedule time for hobbies and rest.\n"
        "3. Learn to say no when needed."
    )
}


class Query(BaseModel):
    question: str

@app.post("/motimo")
def motimo(query: Query):
    q = query.question.lower()
    if q in responses:
        return {"answer": responses[q]}
    else:
        return {"answer": "Hmm 🤔 I don't have that in my list yet — but keep going, you're doing great!"}

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Motimo — your Mini Life Coach! 🚀 Ask your motivational questions at /motimo."}

from fastapi import Query

@app.get("/mcp")
def mcp(question: str = Query(...)):
    q = question.lower()
    if q in responses:
        return {"answer": responses[q]}
    else:
        return {"answer": "Hmm 🤔 I don't have that in my list yet — but keep going, you're doing great!"}

