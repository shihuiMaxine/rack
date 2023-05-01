import statistics

HOME_DIR = "."

STOPWORD_DIR = HOME_DIR + "/pp-data"
MAX_ENT_MODEL_DIR = HOME_DIR + "/models"
MAXAPI = 10
DELTA1 = 10
DELTA2 = 10
alpha = 0.325
beta = 0.575
psi = 0.1
gamma = 0.0
GOLDSET_SIZE = 10
connectionString = "jdbc:sqlite:" + HOME_DIR + "/rack.database/RACK-EMSE.db"

EXP_HOME=connectionString
