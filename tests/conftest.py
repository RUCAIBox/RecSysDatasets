"""Shared pytest fixtures and configuration."""
import os
import tempfile
import shutil
from pathlib import Path
from typing import Generator, Dict, Any

import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'item_id': [100, 200, 300, 400, 500],
        'rating': [5.0, 4.0, 3.0, 2.0, 1.0],
        'timestamp': pd.date_range('2023-01-01', periods=5, freq='D')
    })


@pytest.fixture
def sample_numpy_array() -> np.ndarray:
    """Create a sample numpy array for testing."""
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    """Create a mock configuration dictionary."""
    return {
        'input_path': '/path/to/input',
        'output_path': '/path/to/output',
        'separator': ',',
        'encoding': 'utf-8',
        'chunk_size': 1000,
        'verbose': True
    }


@pytest.fixture
def sample_csv_file(temp_dir: Path) -> Path:
    """Create a sample CSV file for testing."""
    csv_path = temp_dir / 'sample.csv'
    df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': ['a', 'b', 'c'],
        'col3': [1.1, 2.2, 3.3]
    })
    df.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def sample_json_file(temp_dir: Path) -> Path:
    """Create a sample JSON file for testing."""
    import json
    json_path = temp_dir / 'sample.json'
    data = {
        'users': [
            {'id': 1, 'name': 'User1'},
            {'id': 2, 'name': 'User2'}
        ],
        'items': [
            {'id': 100, 'title': 'Item1'},
            {'id': 200, 'title': 'Item2'}
        ]
    }
    with open(json_path, 'w') as f:
        json.dump(data, f)
    return json_path


@pytest.fixture
def mock_dataset_files(temp_dir: Path) -> Dict[str, Path]:
    """Create mock dataset files for testing conversion tools."""
    files = {}
    
    # Create inter file
    inter_path = temp_dir / 'dataset.inter'
    with open(inter_path, 'w') as f:
        f.write("user_id\titem_id\trating\ttimestamp\n")
        f.write("1\t100\t5.0\t1234567890\n")
        f.write("2\t200\t4.0\t1234567891\n")
    files['inter'] = inter_path
    
    # Create user file
    user_path = temp_dir / 'dataset.user'
    with open(user_path, 'w') as f:
        f.write("user_id\tage\tgender\n")
        f.write("1\t25\tM\n")
        f.write("2\t30\tF\n")
    files['user'] = user_path
    
    # Create item file
    item_path = temp_dir / 'dataset.item'
    with open(item_path, 'w') as f:
        f.write("item_id\ttitle\tcategory\n")
        f.write("100\tItem A\tCategory 1\n")
        f.write("200\tItem B\tCategory 2\n")
    files['item'] = item_path
    
    return files


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test."""
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def capture_logs():
    """Capture log messages during tests."""
    import logging
    from io import StringIO
    
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    yield log_capture
    
    logger.removeHandler(handler)


def pytest_configure(config):
    """Configure pytest with custom settings."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )