# src/utils/logger.py
import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Stream console handler forcing UTF-8 wrap for Windows PowerShell
        ch = logging.StreamHandler(sys.stdout)
        if hasattr(sys.stdout, 'reconfigure'):
            try:
                sys.stdout.reconfigure(encoding='utf-8')
            except Exception:
                pass
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        # File handler explicitly forcing UTF-8 encoding
        fh = logging.FileHandler("agent_execution.log", encoding="utf-8")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
    return logger