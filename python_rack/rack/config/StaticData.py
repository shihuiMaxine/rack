import statistics
import rack.config
class StaticData :
    
    HOME_DIR = "."
    STOPWORD_DIR = None
    MAX_ENT_MODEL_DIR = None
    MAXAPI = 0
    DELTA1 = 0
    DELTA2 = 0
    alpha = 0.0
    beta = 0.0
    psi = 0.0
    gamma = 0.0
    GOLDSET_SIZE = 0
    
    def __init__(rack, config):
        rack.config = config   
    statistics
    rack.config.StaticData.STOPWORD_DIR = rack.config.StaticData.HOME_DIR + "/pp-data"
    rack.config.StaticData.MAX_ENT_MODEL_DIR = rack.config.StaticData.HOME_DIR + "/models"
    rack.config.StaticData.MAXAPI = 10
    rack.config.StaticData.DELTA1 = 10
    rack.config.StaticData.DELTA2 = 10
    rack.config.StaticData.alpha = 0.325
    rack.config.StaticData.beta = 0.575
    rack.config.StaticData.psi = 0.1
    rack.config.StaticData.gamma = 0.0
    rack.config.StaticData.GOLDSET_SIZE = 10
    rack.config.StaticData.connectionString = "jdbc:sqlite:" + rack.config.StaticData.HOME_DIR + "/rack.database/RACK-EMSE.db"