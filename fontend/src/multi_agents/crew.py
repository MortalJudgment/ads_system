# crew.py

from crewai import Crew
from agents import get_prompt_analyst, get_researcher, get_domain_expert, get_writer, get_quality_assurance
from tasks import get_prompt_analysis_task, get_research_task, get_expert_analysis_task, get_writing_task, get_qa_task

def get_crew(prompt):
    prompt_analyst = get_prompt_analyst()
    researcher = get_researcher()
    domain_expert = get_domain_expert()
    writer = get_writer()
    qa_agent = get_quality_assurance()

    prompt_analysis_task = get_prompt_analysis_task(prompt, prompt_analyst)
    research_task = get_research_task(prompt, researcher)
    expert_analysis_task = get_expert_analysis_task(prompt, domain_expert)
    writing_task = get_writing_task(prompt, writer)
    qa_task = get_qa_task(prompt, qa_agent)

    return Crew(
        agents=[prompt_analyst, researcher, domain_expert, writer, qa_agent],
        tasks=[prompt_analysis_task, research_task, expert_analysis_task, writing_task, qa_task],
        verbose=2
    )

if __name__ == "__main__":
    prompt = "Explain the impact of artificial intelligence on healthcare in the next decade."
    crew = get_crew(prompt)
    result = crew.kickoff()
    print(result)