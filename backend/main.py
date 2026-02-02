"""
Python AI Tutor - Backend API
FastAPI application for lesson management and progress tracking
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import httpx
import os

# Initialize FastAPI app
app = FastAPI(
    title="Python AI Tutor API",
    description="Backend API for the Python AI Tutor web application",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===================================
# Data Models
# ===================================

class ProgressUpdate(BaseModel):
    """Model for progress update requests"""
    lesson_id: str
    completed: bool


class UserProgress(BaseModel):
    """Model for user progress data"""
    completed_lessons: List[str]
    last_accessed_lesson: Optional[str] = None
    started_date: str
    last_updated: str


class AIChatRequest(BaseModel):
    """Model for AI chat requests"""
    message: str
    lesson_id: Optional[str] = None
    conversation_history: Optional[List[Dict[str, str]]] = []
    provider: str = 'custom'
    api_key: str
    model: Optional[str] = None
    custom_endpoint: Optional[str] = None


# ===================================
# In-Memory Storage (Mock Database)
# Will be replaced with SQLite
# ===================================

# Mock user progress storage
user_progress_store = {}


# ===================================
# API Routes
# ===================================

@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": "Python AI Tutor API",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/api/lessons")
async def get_lessons():
    """Get list of available lessons"""
    lessons = [
        {
            "id": "lesson-01",
            "number": 1,
            "title": "What is Programming?",
            "description": "Understand what programming is and why Python is a great first language to learn.",
            "available": True
        },
        {
            "id": "lesson-02",
            "number": 2,
            "title": "Variables and Data Types",
            "description": "Learn how to store and work with different types of data in Python.",
            "available": True
        },
        {
            "id": "lesson-03",
            "number": 3,
            "title": "Input and Output",
            "description": "Discover how to get information from users and display results.",
            "available": True
        }
    ]
    return {"lessons": lessons}


@app.get("/api/lessons/{lesson_id}")
async def get_lesson(lesson_id: str):
    """Get specific lesson content"""
    # In production, this would load from files or database
    # For now, return basic metadata
    lessons = {
        "lesson-01": {
            "id": "lesson-01",
            "title": "What is Programming?",
            "file": "lesson-01.md"
        },
        "lesson-02": {
            "id": "lesson-02",
            "title": "Variables and Data Types",
            "file": "lesson-02.md"
        },
        "lesson-03": {
            "id": "lesson-03",
            "title": "Input and Output",
            "file": "lesson-03.md"
        }
    }
    
    if lesson_id not in lessons:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    return lessons[lesson_id]


@app.get("/api/progress/{user_id}")
async def get_progress(user_id: str):
    """Get user progress"""
    if user_id not in user_progress_store:
        # Return default progress for new users
        return {
            "completed_lessons": [],
            "last_accessed_lesson": None,
            "started_date": datetime.utcnow().isoformat(),
            "last_updated": datetime.utcnow().isoformat()
        }
    
    return user_progress_store[user_id]


@app.post("/api/progress/{user_id}")
async def update_progress(user_id: str, progress: ProgressUpdate):
    """Update user progress"""
    # Initialize user progress if doesn't exist
    if user_id not in user_progress_store:
        user_progress_store[user_id] = {
            "completed_lessons": [],
            "last_accessed_lesson": None,
            "started_date": datetime.utcnow().isoformat(),
            "last_updated": datetime.utcnow().isoformat()
        }
    
    # Update progress
    if progress.completed and progress.lesson_id not in user_progress_store[user_id]["completed_lessons"]:
        user_progress_store[user_id]["completed_lessons"].append(progress.lesson_id)
    
    user_progress_store[user_id]["last_accessed_lesson"] = progress.lesson_id
    user_progress_store[user_id]["last_updated"] = datetime.utcnow().isoformat()
    
    return {
        "success": True,
        "progress": user_progress_store[user_id]
    }


# ===================================
# AI Tutor Endpoints
# ===================================

@app.post("/api/ai/chat")
async def ai_chat(request: AIChatRequest):
    """
    Proxy AI chat requests to configured provider
    
    This endpoint:
    - Handles CORS (solves browser cross-origin issues)
    - Secures API keys (in future, stored on backend)
    - Enables tier checking (free vs paid - future)
    - Provides consistent interface regardless of AI provider
    """
    
    try:
        # Prepare messages for AI
        messages = request.conversation_history or []
        
        # Call appropriate AI provider
        if request.provider == 'openrouter':
            response = await call_openrouter(
                messages=messages,
                api_key=request.api_key,
                model=request.model or 'meta-llama/llama-3.2-3b-instruct:free'
            )
        elif request.provider == 'openai':
            response = await call_openai(
                messages=messages,
                api_key=request.api_key,
                model=request.model or 'gpt-3.5-turbo'
            )
        elif request.provider == 'anthropic':
            response = await call_anthropic(
                messages=messages,
                api_key=request.api_key,
                model=request.model or 'claude-3-haiku-20240307'
            )
        elif request.provider == 'custom':
            response = await call_custom_endpoint(
                messages=messages,
                api_key=request.api_key,
                endpoint=request.custom_endpoint,
                model=request.model
            )
        else:
            raise HTTPException(status_code=400, detail=f"Unknown provider: {request.provider}")
        
        return {
            "success": True,
            "response": response,
            "provider": request.provider
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def call_openrouter(messages: List[Dict], api_key: str, model: str) -> str:
    """Call OpenRouter API"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'HTTP-Referer': 'http://localhost:8000',
                'X-Title': 'Python AI Tutor'
            },
            json={
                'model': model,
                'messages': messages
            },
            timeout=30.0
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
        data = response.json()
        return data['choices'][0]['message']['content']


async def call_openai(messages: List[Dict], api_key: str, model: str) -> str:
    """Call OpenAI API"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'model': model,
                'messages': messages
            },
            timeout=30.0
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
        data = response.json()
        return data['choices'][0]['message']['content']


async def call_anthropic(messages: List[Dict], api_key: str, model: str) -> str:
    """Call Anthropic (Claude) API"""
    # Separate system message from conversation
    system_msg = next((m['content'] for m in messages if m['role'] == 'system'), '')
    conv_messages = [m for m in messages if m['role'] != 'system']
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'https://api.anthropic.com/v1/messages',
            headers={
                'x-api-key': api_key,
                'anthropic-version': '2023-06-01',
                'Content-Type': 'application/json'
            },
            json={
                'model': model,
                'max_tokens': 1024,
                'messages': conv_messages,
                'system': system_msg
            },
            timeout=30.0
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
        data = response.json()
        return data['content'][0]['text']


async def call_custom_endpoint(messages: List[Dict], api_key: str, endpoint: str, model: Optional[str]) -> str:
    """Call custom API endpoint"""
    if not endpoint:
        raise HTTPException(status_code=400, detail="Custom endpoint URL required")
    
    # Prepare request body (OpenAI-compatible format)
    request_body = {
        'messages': messages
    }
    
    if model:
        request_body['model'] = model
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            endpoint,
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            json=request_body,
            timeout=60.0  # Longer timeout for internal APIs
        )
        
        if response.status_code != 200:
            error_text = response.text
            raise HTTPException(
                status_code=response.status_code, 
                detail=f"Custom API error: {error_text}"
            )
        
        data = response.json()
        
        # Try to extract response (support multiple formats)
        if 'choices' in data:
            # OpenAI-compatible format
            return data['choices'][0]['message']['content']
        elif 'response' in data:
            # Simple format
            return data['response']
        elif 'content' in data:
            # Anthropic-like format
            return data['content'][0]['text'] if isinstance(data['content'], list) else data['content']
        else:
            # Return whole response as fallback
            return str(data)


# ===================================
# Development Server
# ===================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

