from sqlalchemy import (
    Column ,
    Integer ,
    String ,
    Boolean ,
    Date ,
    Time ,
    func , 
    ForeignKey ,
    UniqueConstraint ,
)
from .db import BaseModel , engine , relationship


class Agent(BaseModel):
    """
    Attributes :-
        - id auto
        - name  * required
        - deleted  default 0
        - active default 1 
        - created_date  auto
        - created_time  auto

    [*] live_data
    """
    __tablename__ = "agents"
    id = Column(Integer,primary_key=True)
    name = Column(String(50) , nullable=False)
    deleted = Column(Boolean , default = False , nullable=False)
    active = Column(Boolean, default =True, nullable=False)
    created_date = Column(Date,server_default=func.current_date())
    created_time = Column(Time ,server_default=func.current_time())
    # live_data = relationship("RowOfLiveData" , back_populates="agent")
    # live_data = relationship("RowOfLiveData", back_populates="agent")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id = {self.id} , name = {self.name})"


class Project(BaseModel):
    """
    Attributes :-
        - id auto
        - name  * required
        - extension * required
        - deleted  default 0
        - active default 1 
        - created_date  auto
        - created_time  auto
    [*] live_data
    """
    __tablename__ = "projects"
    id = Column(Integer,primary_key=True)
    name = Column(String(50) , nullable=False)
    extension = Column(String(10),nullable=False)
    deleted = Column(Boolean , default = False , nullable=False)
    active = Column(Boolean, default =True, nullable=False)
    created_date = Column(Date,server_default=func.current_date())
    created_time = Column(Time ,server_default=func.current_time())
    # live_data = relationship("RowOfLiveData" , back_populates="project")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id = {self.id} , name = {self.name})"


class Source(BaseModel):
    """
    Attributes :-
        - id auto
        - name  * required
        - deleted  default 0
        - active default 1 
        - created_date  auto
        - created_time  auto
    """
    __tablename__ = "sources"
    id = Column(Integer,primary_key=True)
    name = Column(String(50) , nullable=False)
    deleted = Column(Boolean , default = False , nullable=False)
    active = Column(Boolean, default =True, nullable=False)
    created_date = Column(Date,server_default=func.current_date())
    created_time = Column(Time ,server_default=func.current_time())
    # data = relationship("RowOfData" , back_populates="source")
    # leads = relationship("Lead",back_populates="source")
    # live_data = relationship("RowOfLiveData" , back_populates="source")
    # live_data = relationship("RowOfLiveData", back_populates="source")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id = {self.id} , name = {self.name})"



class RowOfData(BaseModel):
    """
    Attributes :-
    - number  * required
    - source_id  * required
    - name (optional) NULL
    - taken default 0
    - deleted default 0
    - registered default 0
    - created_date  auto
    - created_time  auto
    """
    __tablename__ = "data"
    id = Column(Integer,primary_key=True)
    deleted = Column(Boolean , default = False , nullable=False)
    name = Column(String(50),nullable=True)
    taked = Column(Boolean , default=False )
    number = Column(String(20),nullable=False,unique=True)
    source_id = Column(Integer , ForeignKey("sources.id"))
    created_date = Column(Date,server_default=func.current_date())
    created_time = Column(Time ,server_default=func.current_time())
    # source = relationship("Source",back_populates="datarows")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id = {self.id} , name = {self.name})"
    __table_args__ = (
        UniqueConstraint('number'),
    )


class RowOfLiveData(BaseModel): 
    """
    Attributes :-
        - id 
        - agent_id 
        - agent 
        - number
        - project_id 
        - project 
        - source_id 
        - source 
        - created_date 
        - created_time 
    """
    __tablename__ = "live_data"
    id = Column(Integer,primary_key=True)
    # agent_id = Column(Integer , ForeignKey("agents.id"))
    # agent = relationship("Agent",back_populates="live_data")
    agent_id = Column(Integer, ForeignKey("agents.id"))
    # agent = relationship("Agent", back_populates="live_data")

    number = Column(String(20),nullable=False)
    # project_id = Column(Integer , ForeignKey("projects.id"))
    # project = relationship("Project",back_populates="live_data")
    project_id = Column(Integer, ForeignKey("projects.id"))
    # project = relationship("Project", back_populates="live_data")

    # source_id = Column(Integer , ForeignKey("sources.id"))
    # source = relationship("Source",back_populates="live_data")
    source_id = Column(Integer, ForeignKey("sources.id"))
    # source = relationship("Source", back_populates="live_data")

    # lead = relationship("Lead", uselist=False, back_populates="row_of_live_data")

    created_date = Column(Date,server_default=func.current_date())
    created_time = Column(Time ,server_default=func.current_time())

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id = {self.id} , number = {self. number})"




class Lead(BaseModel):
    """
    Attributes :-
    - live_data_id  * required
    - number  * required
    - name (optional) NULL
    - deleted default 0
    - description (optional) NULL
    - created_date  auto
    - created_time  auto
    """
    __tablename__ = "leads"
    id = Column(Integer,primary_key=True)
    name = Column(String(20) , nullable=True)
    description = Column(String(100) , nullable=True)
    deleted = Column(Boolean , default = False , nullable=False)
    created_date = Column(Date,server_default=func.current_date())
    created_time = Column(Time ,server_default=func.current_time())
    live_data_id = Column(Integer ,ForeignKey("live_data.id"))
    # row_of_live_data = relationship("RowOfLiveData", uselist=False, back_populates="lead")


    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id = {self.id} , name = {self.name})"


BaseModel.metadata.create_all(bind=engine)