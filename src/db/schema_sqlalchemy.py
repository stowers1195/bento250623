# schema_sqlalchemy.py
"""
The SQLAlchemy-style python class representation of the Bento SQL schema.
"""

from typing import KeysView
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String, Time, create_engine, func
from sqlalchemy.orm import relationship, sessionmaker
from datetime import date, datetime
import enum
from os.path import expanduser, exists, sep

Base = declarative_base()

class SexEnum(enum.Enum):
    M = "Male"
    F = "Female"
    U = "Unknown"

class Animal(Base):
    """ mapper for the animal table """
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True)
    animal_services_id = Column(Integer)
    dob = Column(Date)
    sex = Column(Enum(SexEnum))     # SexEnum.M, F or U
    genotype = Column(String(128))  # genetic strain
    nickname = Column(String(128))  # investigator-specific identifier
    investigator_id = Column(Integer, ForeignKey('investigator.id'))
    sessions = relationship("Session")
    surgeries = relationship("Surgery",
        cascade='all, delete, delete-orphan')

    def __repr__(self):
        return "<Animal(asid='%d', nickname='%s', dob='%s', sex='%s', genotype='%s')>" % (
            self.animal_services_id, self.nickname, self.dob, self.sex, self.genotype)

class Investigator(Base):
    """ mapper for the investigator table """
    __tablename__ = 'investigator'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(32))
    last_name = Column(String(64))
    first_name = Column(String(64))
    institution = Column(String(64))
    e_mail = Column(String(128))
    sessions = relationship('Session')
    animals = relationship('Animal')

    def __repr__(self):
        return "<Investigator(user_name='%s', last_name='%s', first_name='%s', institution='%s', e_mail='%s')>" % (
            self.user_name, self.last_name, self.first_name, self.institution, self.e_mail
        )

class Camera(Base):
    """ mapper for the camera table """
    __tablename__ = 'camera'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    model = Column(String(128))
    lens = Column(String(128))
    position = Column(String(128))
    videos = relationship('VideoData', back_populates='camera')

    def __repr__(self):
        return "<Camera(id='%d', name='%s', model='%s', kebs='%s', position='%s')>" % (
            self.id, self.name, self.model, self.lens, self.position
        )

class NeuralData(Base):
    """
    Mapper for neural_data table
    """
    __tablename__ = 'neural_data'

    id = Column(Integer, primary_key=True)
    file_path = Column(String(512))
    sample_rate = Column(Float)
    format = Column(String(128))
    offset_time = Column(Float)   # needs to be convertible to timecode
    start_frame = Column(Integer)
    stop_frame = Column(Integer)
    trial = Column(Integer, ForeignKey('trial.id'))   # 'Trial.trial_id' is quoted because it's a forward reference
    keys = ['id', 'Neural File Path', 'Sample Rate', 'Format', 'Offset Time', 'Start Frame', 'Stop Frame', 'trial_id']

    def __init__(self, d=None, db_sess=None):
        super().__init__()
        if d and db_sess:
            self.fromDict(d, db_sess)

    def __repr__(self):
        return "<NeuralData(file_path='%s', sample_rate='%f', format='%s', offset_time='%f', start_frame='%d', stop_frame='%d')>" % (
            self.file_path, self.sample_rate, self.format, self.offset_time, self.start_frame, self.stop_frame
        )

    def header(self):
        return self.keys

    def toDict(self):
        return {
            'id': self.id,
            'Neural File Path': self.file_path,
            'Sample Rate': self.sample_rate,
            'Format': self.format,
            'Offset Time': self.offset_time,
            'Start Frame': self.start_frame,
            'Stop Frame': self.stop_frame,
            'trial_id': self.trial
        }

    def fromDict(self, d, db_sess):
        # only update fields that have changed to cut down on DB transactions
        if not set(d.keys()).issuperset(set(self.keys)):
            raise RuntimeError("Dict provided has incorrect or incomplete contents")
        if 'id' in d.keys() and d['id'] and d['id'] != self.id:
            self.id = d['id']
        if 'Neural File Path' in d.keys() and d['Neural File Path'] != self.file_path:
            self.file_path = d['Neural File Path']
        if 'Sample Rate' in d.keys() and d['Sample Rate'] != self.sample_rate:
            self.sample_rate = d['Sample Rate']
        if 'Format' in d.keys() and d['Format'] != self.format:
            self.format = d['Format']
        if 'Offset Time' in d.keys() and d['Offset Time'] != self.offset_time:
            self.offset_time = d['Offset Time']
        if 'Start Frame' in d.keys() and d['Start Frame'] != self.start_frame:
            self.start_frame = d['Start Frame']
        if 'Stop Frame' in d.keys() and d['Stop Frame'] != self.stop_frame:
            self.stop_frame = d['Stop Frame']
        if 'trial_id' in d.keys() and d['trial_id'] != self.trial:
            self.trial = d['trial_id']

class VideoData(Base):
    """
    Mapper for video_data table
    """
    __tablename__ = 'video_data'

    id = Column(Integer, primary_key=True)
    file_path = Column(String(512))
    sample_rate = Column(Float)
    offset_time = Column(Float)   # needs to be convertible to timecode
    camera_id = Column(Integer, ForeignKey('camera.id'))
    trial = Column(Integer, ForeignKey('trial.id'))
    camera = relationship('Camera')
    pose_data = relationship('PoseData')
    # don't put id first, because then we can't hide it in a QTreeWidget as column 0
    keys = ['Video File Path', 'Sample Rate', 'Offset Time', 'Camera Position', 'trial_id', 'id']

    def __init__(self, d=None, db_sess=None):
        super().__init__()
        if d and db_sess:
            self.fromDict(d, db_sess)

    def __repr__(self):
        return "<VideoData(file_path='%s', sample_rate='%s', offset_time='%s')>" % (
            self.file_path, self.sample_rate, self.offset_time
        )

    def header(self):
        return self.keys

    def toDict(self):
        pose_data = [elem.toDict() for elem in self.pose_data]
        return {
            'id': self.id,
            'Video File Path': self.file_path,
            'Sample Rate': self.sample_rate,
            'Offset Time': self.offset_time,
            'Camera Position': self.camera.position,
            'trial_id': self.trial,
            'pose_data': pose_data
            #TODO: camera?
        }

    def fromDict(self, d, db_sess):
        # only update fields that have changed to cut down on DB transactions
        if not set(d.keys()).issuperset(set(self.keys)):
            raise RuntimeError("Dict provided has incorrect or incomplete contents")
        camera = db_sess.query(Camera).where(func.lower(Camera.position) == func.lower(d['Camera Position'])).scalar()
        if not camera:
            raise RuntimeError(f"No camera with position {d['Camera Position']}")
        if 'id' in d.keys() and d['id'] and d['id'] != self.id:
            self.id = d['id']
        if 'Video File Path' in d.keys() and d['Video File Path'] != self.file_path:
            self.file_path = d['Video File Path']
        if 'Sample Rate' in d.keys() and d['Sample Rate'] != self.sample_rate:
            self.sample_rate = d['Sample Rate']
        if 'Offset Time' in d.keys() and d['Offset Time'] != self.offset_time:
            self.offset_time = d['Offset Time']
        if self.camera_id != camera.id:
            self.camera_id = camera.id
        if self.camera != camera:
            self.camera = camera
        if 'trial_id' in d.keys() and d['trial_id'] != self.trial:
            self.trial = d['trial_id']
        #TODO: pose_data?

class AnnotationsData(Base):
    """
    Mapper for annotations table
    """
    __tablename__ = 'annotations'

    id = Column(Integer, primary_key=True)
    file_path = Column(String(512))
    sample_rate = Column(Float)
    format = Column(String(128), nullable=False)
    offset_time = Column(Float)   # needs to be convertible to timecode
    start_frame = Column(Integer)
    stop_frame = Column(Integer)
    annotator_name = Column(String(128))
    method = Column(String(128))   # e.g. manual, MARS v1_8
    trial = Column(Integer, ForeignKey('trial.id'))
    keys = ['id', 'Annotations File Path', 'Sample Rate', 'Format', 'Offset Time', 'Start Frame',
            'Stop Frame', 'Annotator Name', 'Method', 'trial_id']

    def __init__(self, d=None, db_sess=None):
        super().__init__()
        if d and db_sess:
            self.fromDict(d, db_sess)

    def __repr__(self):
        return ( "<AnnotationsData(file_path='%s', sample_rate='%s', format='%s',"
            " offset_time='%s', start_frame='%s', stop_frame='%s',"
            " annotator_name='%s', method='%s')>" % (
            self.file_path, self.sample_rate, self.format,
            self.offset_time, self.start_frame, self.stop_frame,
            self.annotator_name, self.method )
        )

    def header(self):
        return self.keys

    def toDict(self):
        return {
            'id': self.id,
            'Annotations File Path': self.file_path,
            'Sample Rate': self.sample_rate,
            'Format': self.format,
            'Offset Time': self.offset_time,
            'Start Frame': self.start_frame,
            'Stop Frame': self.stop_frame,
            'Annotator Name': self.annotator_name,
            'Method': self.method,
            'trial_id': self.trial
        }

    def fromDict(self, d, db_sess):
        # only update fields that have changed to cut down on DB transactions
        if not set(d.keys()).issuperset(set(self.keys)):
            raise RuntimeError("Dict provided has incorrect or incomplete contents")
        if 'id' in d.keys() and d['id'] and d['id'] != self.id:
            self.id = d['id']
        if 'Annotations File Path' in d.keys() and d['Annotations File Path'] != self.file_path:
            self.file_path = d['Annotations File Path']
        if 'Sample Rate' in d.keys() and d['Sample Rate'] != self.sample_rate:
            self.sample_rate = d['Sample Rate']
        if 'Format' in d.keys() and d['Format'] != self.format:
            self.format = d['Format']
        if 'Offset Time' in d.keys() and d['Offset Time'] != self.offset_time:
            self.offset_time = d['Offset Time']
        if 'Start Frame' in d.keys() and d['Start Frame'] != self.start_frame:
            self.start_frame = d['Start Frame']
        if 'Stop Frame' in d.keys() and d['Stop Frame'] != self.stop_frame:
            self.stop_frame = d['Stop Frame']
        if 'Annotator Name' in d.keys() and d['Annotator Name'] != self.annotator_name:
            self.annotator_name = d['Annotator Name']
        if 'Method' in d.keys() and d['Method'] != self.method:
            self.method = d['Method']
        if 'trial_id' in d.keys() and d['trial_id'] != self.trial:
            self.trial = d['trial_id']

class AudioData(Base):
    """
    Mapper for audio_data table
    """
    __tablename__ = 'audio_data'

    id = Column(Integer, primary_key=True)
    file_path = Column(String(512))
    sample_rate = Column(Float)
    offset_time = Column(Float)   # needs to be convertible to timecode
    processed_audio_file_path = Column(String(512))
    # annotations_id = Column(Integer, ForeignKey('annotations.id'))
    trial = Column(Integer, ForeignKey('trial.id'))
    # keys = ['id', 'file_path', 'sample_rate', 'offset_time', 'processed_audio_file_path', 'annotations_id', 'trial_id']
    keys = ['id', 'Audio File Path', 'Sample Rate', 'Offset Time', 'Processed Audio File Path', 'trial_id']

    def __init__(self, d=None, db_sess=None):
        super().__init__()
        if d and db_sess:
            self.fromDict(d, db_sess)

    def __repr__(self):
        return ( "<AudioData(file_path='%s', sample_rate='%s', offset_time='%s',"
            " start_frame='%s', stop_frame='%s', processed_audio_file_path='%s')>" % (
            self.file_path, self.sample_rate, self.offset_time,
            self.start_frame, self.stop_time, self.processed_audio_file_path )
        )

    def header(self):
        return self.keys

    def toDict(self):
        return {
            'id': self.id,
            'Audio File Path': self.file_path,
            'Sample Rate': self.sample_rate,
            'Offset Time': self.offset_time,
            'Processed Audio File Path': self.processed_audio_file_path,
            # 'annotations_id': self.annotations_id,
            'trial_id': self.trial
        }

    def fromDict(self, d, db_sess):
        # only update fields that have changed to cut down on DB transactions
        if not set(d.keys()).issuperset(set(self.keys)):
            raise RuntimeError("Dict provided has incorrect or incomplete contents")
        if 'id' in d.keys() and d['id'] and d['id'] != self.id:
            self.id = d['id']
        if 'Audio File Path' in d.keys() and d['Audio File Path'] != self.file_path:
            self.file_path = d['Audio File Path']
        if 'Sample Rate' in d.keys() and d['Sample Rate'] != self.sample_rate:
            self.sample_rate = d['Sample Rate']
        if 'Offset Time' in d.keys() and d['Offset Time'] != self.offset_time:
            self.offset_time = d['Offset Time']
        if ('Processed Audio File Path' in d.keys()
            and d['Processed Audio File Path'] != self.processed_audio_file_path):
            self.processed_audio_file_path = d['Processed Audio File Path']
        # if 'annotations_id' in d.keys() and d['annotations_id'] != self.annotations_id:
            # self.annotations_id = d['annotations_id']
        if 'trial_id' in d.keys() and d['trial_id'] != self.trial:
            self.trial = d['trial_id']

class PoseData(Base):
    """
    Mapper for pose_data table
    """
    __tablename__ = 'pose_data'

    pose_id = Column(Integer, primary_key=True)
    file_path = Column(String(512))
    sample_rate = Column(Float)
    offset_time = Column(Float)   # needs to be convertible to timecode
    format = Column(String(128), nullable=False)
    video = Column(Integer, ForeignKey('video_data.id'))
    trial = Column(Integer, ForeignKey('trial.id'))
    # don't put id first, because then we can't hide it in a QTreeWidget as column 0
    keys = ['Pose File Path', 'Sample Rate', 'Offset Time', 'Format', 'video_id', 'trial_id', 'id']

    def __init__(self, d=None, db_sess=None):
        super().__init__()
        if d and db_sess:
            self.fromDict(d, db_sess)

    def __repr__(self):
        return ( "<PoseData(file_path='%s', sample_rate='%s', offset_time='%s',"
            " format='%s')>" % (
            self.file_path, self.sample_rate, self.offset_time, self.format )
        )

    def header(self):
        return self.keys

    def toDict(self):
        return {
            'id': self.pose_id,
            'Pose File Path': self.file_path,
            'Sample Rate': self.sample_rate,
            'Offset Time': self.offset_time,
            'Format': self.format,
            'video_id': self.video,
            'trial_id': self.trial
        }

    def fromDict(self, d, db_sess):
        # only update fields that have changed to cut down on DB transactions
        if not set(d.keys()).issuperset(set(self.keys)):
            raise RuntimeError("Dict provided has incorrect or incomplete contents")
        if 'id' in d.keys() and d['id'] and d['id'] != self.pose_id:
            self.pose_id = d['id']
        if 'Pose File Path' in d.keys() and d['Pose File Path'] != self.file_path:
            self.file_path = d['Pose File Path']
        if 'Sample Rate' in d.keys() and d['Sample Rate'] != self.sample_rate:
            self.sample_rate = d['Sample Rate']
        if 'Offset Time' in d.keys() and d['Offset Time'] != self.offset_time:
            self.offset_time = d['Offset Time']
        if 'Format' in d.keys() and d['Format'] != self.format:
            self.format = d['Format']
        if 'video_id' in d.keys() and d['video_id'] != self.video:
            self.video = d['video_id']
        if 'trial_id' in d.keys() and d['trial_id'] != self.trial:
            self.trial = d['trial_id']

class OtherData(Base):
    """
    Mapper for other_data table
    """
    __tablename__ = 'other_data'

    id = Column(Integer, primary_key=True)
    file_path = Column(String(512))
    sample_rate = Column(Float)
    offset_time = Column(Float)   # needs to be convertible to timecode
    start_frame = Column(Integer)
    stop_frame = Column(Integer)
    format = Column(String(128))
    trial = Column(Integer, ForeignKey('trial.id'))
    keys = ['id', 'File Path', 'Sample Rate', 'Offset Time', 'Start Frame', 'Stop Frame', 'Format', 'trial_id']

    def __init__(self, d=None, db_sess=None):
        super().__init__()
        if d and db_sess:
            self.fromDict(d, db_sess)

    def __repr__(self):
        return ( "<OtherData(file_path='%s', sample_rate='%s', offset_time='%s',"
            " start_frame='%s', stop_frame='%s', format='%s')>" % (
            self.file_path, self.sample_rate, self.offset_time,
            self.offset_time, self.stop_frame, self.format )
        )

    def header(self):
        return self.keys

    def toDict(self):
        return {
            'id': self.id,
            'File Path': self.file_path,
            'Sample Rate': self.sample_rate,
            'Offset Time': self.offset_time,
            'Start Frame': self.start_frame,
            'Stop Frame': self.stop_frame,
            'Format': self.format,
            'trial_id': self.trial
        }

    def fromDict(self, d, db_sess):
        # only update fields that have changed to cut down on DB transactions
        if not set(d.keys()).issuperset(set(self.keys)):
            raise RuntimeError("Dict provided has incorrect or incomplete contents")
        if 'id' in d.keys() and d['id'] and d['id'] != self.id:
            self.id = d['id']
        if 'File Path' in d.keys() and d['File Path'] != self.file_path:
            self.file_path = d['File Path']
        if 'Sample Rate' in d.keys() and d['Sample Rate'] != self.sample_rate:
            self.sample_rate = d['Sample Rate']
        if 'Offset Time' in d.keys() and d['Offset Time'] != self.offset_time:
            self.offset_time = d['Offset Time']
        if 'Start Frame' in d.keys() and d['Start Frame'] != self.start_frame:
            self.start_frame = d['Start Frame']
        if 'Stop Frame' in d.keys() and d['Stop Frame'] != self.stop_frame:
            self.stop_frame = d['Stop Frame']
        if 'Format' in d.keys() and d['Format'] != self.format:
            self.format = d['Format']
        if 'trial_id' in d.keys() and d['trial_id'] != self.trial:
            self.trial = d['trial_id']

class Session(Base):
    """
    Mapper for session table
    """

    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey('animal.id'), nullable=False)
    investigator_id = Column(Integer, ForeignKey('investigator.id'), nullable=False)
    base_directory = Column(String(512))
    experiment_date = Column(Date)
    session_num = Column(Integer)
    trials = relationship('Trial',
        cascade='all, delete, delete-orphan')

    def __repr__(self):
        return ( "<Session(experiment_date='%s',"
            " session_num='%d', animal_id='%s'>" % (
            ( self.experiment_date.isoformat()
                if isinstance(self.experiment_date, date)
                else self.experiment_date ),
            self.session_num, self.animal_id )
        )

class Trial(Base):
    """
    Mapper for trial table
    """
    __tablename__ = 'trial'

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('session.id'))
    trial_num = Column(Integer)
    trial_start_time = Column(Float)
    stimulus = Column(String(128))
    video_data = relationship('VideoData',
        cascade='all, delete, delete-orphan')    # could be more than one, e.g. top view, front view
    audio_data = relationship('AudioData',
        cascade='all, delete, delete-orphan')    # could be zero or more
    neural_data = relationship('NeuralData',
        cascade='all, delete, delete-orphan')
    pose_data = relationship('PoseData',
        cascade='all, delete, delete-orphan')
    annotations = relationship('AnnotationsData',
        cascade='all, delete, delete-orphan')
    other_data = relationship('OtherData',
        cascade='all, delete, delete-orphan')

    def __repr__(self):
        return "<Trial(session_id='%d', trial_num='%d', stimulus='%s'" % (
            ( self.session_id, self.trial_num, self.stimulus )
        )

class LateralityEnum(enum.Enum):
    Nothing = ""
    Left = "Left"
    Right = "Right"
    Bilateral = "Bilateral"

class Surgery(Base):
    """
    Mapper for surgery table
    """
    __tablename__ = 'surgery'

    animal_id = Column(Integer, ForeignKey('animal.id'), primary_key=True)
    investigator_id = Column(Integer, ForeignKey('investigator.id'), primary_key=True)
    date = Column(Date, primary_key=True)
    implant_side = Column(Enum(LateralityEnum), default=LateralityEnum.Nothing)
    injection_side = Column(Enum(LateralityEnum), default=LateralityEnum.Nothing)
    procedure = Column(String(128))
    anesthesia = Column(String(128))
    follow_up_care = Column(String(128))

    def __repr__(self):
        return ( "<Surgery(date='%s', implant_side='%s', injection_side='%s',"
            " procedure='%s', follow_up_care='%s')>" % (
            self.date.isoformat(), self.implant_side, self.injection_side,
            self.procedure, self.follow_up_care )
        )

def new_session(username, password, host, port, use_personal_db=False):
    need_to_create_tables = False
    if use_personal_db:
        bento_db_file = expanduser("~") + sep + '.bento' + sep + "bento.db"
        if not exists(bento_db_file):
            need_to_create_tables = True    # but only after SqlAlchemy creates the file
        bento_engine = create_engine(f"sqlite:///" + bento_db_file)
    else:
        bento_engine = create_engine(f"mysql+mysqldb://{username}:{password}@{host}:{port}/bento")
    db_sessionMaker = sessionmaker(bind=bento_engine)
    if need_to_create_tables:
        with db_sessionMaker() as db_sess:
            create_tables(db_sess)
    return db_sessionMaker

def create_tables(session):
    Base.metadata.create_all(session.get_bind())
