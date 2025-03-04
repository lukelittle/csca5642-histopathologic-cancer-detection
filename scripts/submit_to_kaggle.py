#!/usr/bin/env python3
"""
Submit a prediction file to the Kaggle competition.

This script submits a prediction file to the Kaggle competition using the Kaggle CLI.
"""

import os
import sys
import argparse
import subprocess

def submit_to_kaggle(submission_file, competition_name="nlp-getting-started", message=None):
    """
    Submit a prediction file to the Kaggle competition.
    
    Args:
        submission_file (str): Path to the submission CSV file
        competition_name (str): Name of the Kaggle competition
        message (str, optional): Message to include with the submission
    
    Returns:
        bool: True if submission was successful, False otherwise
    """
    # Check if submission file exists
    if not os.path.isfile(submission_file):
        print(f"Error: Submission file '{submission_file}' not found.")
        return False
    
    # Build the command
    command = ["kaggle", "competitions", "submit", 
               "-c", competition_name, 
               "-f", submission_file]
    
    # Add message if provided
    if message:
        command.extend(["-m", message])
    
    # Execute the command
    print(f"Submitting {submission_file} to Kaggle competition '{competition_name}'...")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("Submission successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during submission: {e}")
        print(e.stderr)
        return False

def main():
    """Main function to parse arguments and submit to Kaggle."""
    parser = argparse.ArgumentParser(description='Submit a prediction file to the Kaggle competition.')
    parser.add_argument('--file', '-f', default='submission.csv', help='Path to the submission CSV file')
    parser.add_argument('--competition', '-c', default='nlp-getting-started', help='Name of the Kaggle competition')
    parser.add_argument('--message', '-m', help='Message to include with the submission')
    
    args = parser.parse_args()
    
    # Submit to Kaggle
    success = submit_to_kaggle(args.file, args.competition, args.message)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
