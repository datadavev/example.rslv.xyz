"""
Module script for example.
"""
import sys
import uvicorn

def serve() -> int:
    uvicorn.run("example.app:app", host="127.0.0.1", port=3000, log_level="info", reload=True)
    return 0


def main()->int:
    return serve()


if __name__ == "__main__":
    sys.exit(main())