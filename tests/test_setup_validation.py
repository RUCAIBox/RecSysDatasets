"""Validation tests to ensure testing infrastructure is properly configured."""
import pytest
import tempfile
from pathlib import Path
import pandas as pd
import numpy as np


class TestInfrastructureSetup:
    """Test class to validate the testing infrastructure."""
    
    @pytest.mark.unit
    def test_pytest_is_working(self):
        """Verify that pytest is installed and working."""
        assert True
    
    @pytest.mark.unit
    def test_fixtures_are_available(self, temp_dir, sample_dataframe, mock_config):
        """Verify that fixtures from conftest.py are accessible."""
        assert isinstance(temp_dir, Path)
        assert temp_dir.exists()
        
        assert isinstance(sample_dataframe, pd.DataFrame)
        assert len(sample_dataframe) == 5
        
        assert isinstance(mock_config, dict)
        assert 'input_path' in mock_config
    
    @pytest.mark.unit
    def test_markers_are_registered(self):
        """Verify that custom markers are properly registered."""
        # This test itself uses the unit marker
        assert hasattr(self.test_markers_are_registered, 'pytestmark')
    
    @pytest.mark.integration
    def test_file_operations(self, temp_dir):
        """Test that file operations work in temporary directory."""
        test_file = temp_dir / 'test.txt'
        test_file.write_text('Hello, testing!')
        
        assert test_file.exists()
        assert test_file.read_text() == 'Hello, testing!'
    
    @pytest.mark.unit
    def test_numpy_operations(self, sample_numpy_array):
        """Verify numpy is available and working."""
        assert isinstance(sample_numpy_array, np.ndarray)
        assert sample_numpy_array.shape == (3, 3)
        assert np.sum(sample_numpy_array) == 45
    
    @pytest.mark.unit
    def test_pandas_operations(self, sample_dataframe):
        """Verify pandas is available and working."""
        assert 'user_id' in sample_dataframe.columns
        assert sample_dataframe['rating'].mean() == 3.0
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that can be marked as slow."""
        import time
        # Simulate a slow operation
        time.sleep(0.1)
        assert True
    
    @pytest.mark.unit
    def test_mock_capabilities(self, mocker):
        """Verify pytest-mock is working."""
        mock_func = mocker.Mock(return_value=42)
        assert mock_func() == 42
        mock_func.assert_called_once()
    
    @pytest.mark.integration
    def test_csv_file_fixture(self, sample_csv_file):
        """Test the CSV file fixture."""
        assert sample_csv_file.exists()
        df = pd.read_csv(sample_csv_file)
        assert len(df) == 3
        assert list(df.columns) == ['col1', 'col2', 'col3']
    
    @pytest.mark.integration
    def test_json_file_fixture(self, sample_json_file):
        """Test the JSON file fixture."""
        import json
        assert sample_json_file.exists()
        with open(sample_json_file) as f:
            data = json.load(f)
        assert 'users' in data
        assert 'items' in data
    
    @pytest.mark.integration
    def test_mock_dataset_files(self, mock_dataset_files):
        """Test the mock dataset files fixture."""
        assert 'inter' in mock_dataset_files
        assert 'user' in mock_dataset_files
        assert 'item' in mock_dataset_files
        
        for file_type, file_path in mock_dataset_files.items():
            assert file_path.exists()
            assert file_path.stat().st_size > 0


class TestCoverageConfiguration:
    """Tests to verify coverage configuration."""
    
    @pytest.mark.unit
    def test_this_file_is_covered(self):
        """Ensure this test file contributes to coverage."""
        x = 1 + 1
        assert x == 2
    
    @pytest.mark.unit
    def test_coverage_excludes_work(self):
        """Test that coverage exclusion patterns work."""
        # This should be covered
        result = 10 * 2
        assert result == 20
        
        # The following would be excluded by coverage
        if 0:  # pragma: no cover
            raise AssertionError("This should never run")


def test_module_level_test():
    """Test that module-level tests are discovered."""
    assert 2 + 2 == 4