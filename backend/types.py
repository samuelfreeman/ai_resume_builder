from pydantic import BaseModel
from typing import List, Optional

class SignUpRequest(BaseModel):
    fullname: str
    email:str
    password:str

class LoginRequest(BaseModel):
    email: str
    password:str

class Experience(BaseModel):
    company: str
    role: str
    start_date: str
    end_date: Optional[str]
    description:Optional[str]
    responsibilities: List[str]


class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_year: int
    end_year: Optional[int]


class Project(BaseModel):
    name: str
    description: str
    technologies: List[str]

class ResumeRequest(BaseModel):
    # personal info 
    fullname:str
    email: str
    phone:str
    location:str
    linkedin: Optional[str]
    github: Optional[str]

    # Professional data
    summary: Optional[str]
    experiences: List[Experience]
    education: List[Education]
    skills: List[str]
    projects: Optional[List[Project]]

    # AI-specific controls
    job_description: Optional[str]
    tone: Optional[str] = "professional"
    experience_level: Optional[str] = "mid"
    template: Optional[str] = "modern"
    optimize_for_ats: bool = True
