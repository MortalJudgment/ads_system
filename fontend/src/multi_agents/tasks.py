# tasks.py

from textwrap import dedent
from crewai import Task

def get_prompt_analysis_task(prompt, agent):
    return Task(
        description=f"Analyze the following prompt: '{prompt}'. Identify key points, intent, and translate if necessary.",
        agent=agent,
        expected_output="Detailed analysis of the user's prompt, including key points and any necessary translations."
    )

def get_research_task(prompt, agent):
    return Task(
        description=f"Research information related to: {prompt}",
        agent=agent,
        expected_output="Comprehensive research report on the given topic, including relevant facts and sources."
    )

def get_expert_analysis_task(prompt, agent):
    return Task(
        description=f"Provide expert analysis and insights on the topic: {prompt}",
        agent=agent,
        expected_output="In-depth analysis with domain-specific insights and expert opinions."
    )

def get_writing_task(prompt, agent):
    return Task(
        description=f"Write a detailed response to: {prompt}. Use the research and expert analysis provided.",
        agent=agent,
        expected_output="Clear, engaging, and informative response based on the research and expert analysis."
    )

def get_qa_task(prompt, agent):
    return Task(
        description=f"Review the final response to: {prompt}. Ensure accuracy, completeness, and clarity.",
        agent=agent,
        expected_output="Quality assurance report with suggestions for improvements and fact-checking results."
    )