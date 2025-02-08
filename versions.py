import tensorflow
import numpy as np
import PIL
import fastapi
import uvicorn

import sys
print(sys.executable)


print("TensorFlow:", tensorflow.__version__)
print("NumPy:", np.__version__)
print("PIL:", PIL.__version__)
print("FastAPI:", fastapi.__version__)
print("Uvicorn:", uvicorn.__version__)
