import os
from textwrap import dedent
from crewai import Agent
from tools import SerperSearchTool
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def get_llm(model_name):
    return ChatGoogleGenerativeAI(model=model_name,
                                  verbose=True,
                                  temperature=0.5)

def get_prompt_analyst():
    return Agent(
        role='Prompt Analyst',
        goal='Understand and analyze user prompts',
        backstory='You are an AI language expert skilled in interpreting user queries and identifying key points.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm("gemini-1.5-flash")  # Fast processing for quick analysis
    )

def get_researcher():
    return Agent(
        role='Researcher',
        goal='Gather comprehensive and accurate information',
        backstory='You are an AI research assistant with access to vast knowledge and search capabilities.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm("gemini-1.5-flash") 
    )

def get_domain_expert():
    return Agent(
        role='Domain Expert',
        goal='Provide specialized knowledge and insights',
        backstory='You are an AI with deep expertise across various domains, capable of providing nuanced understanding.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm("gemini-1.5-pro")  # Complex reasoning and specialized knowledge
    )

def get_writer():
    return Agent(
        role='Writer',
        goal='Craft clear, engaging, and informative responses',
        backstory='You are an AI writing assistant skilled in communication and content creation.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm("gemini-1.5-flash")  
    )

def get_quality_assurance():
    return Agent(
        role='Quality Assurance',
        goal='Ensure accuracy, completeness, and clarity of the final output',
        backstory='You are an AI reviewer with a keen eye for detail and fact-checking abilities.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm("gemini-1.5-flash")  # Thorough analysis and fact-checking
    )