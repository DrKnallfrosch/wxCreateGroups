# GroupCalculator Project

## Project Status

The **GroupCalculator** project is currently in an **incomplete state**. While significant progress has been made, some core functionalities, such as the group creation feature, are not fully operational. Below is a summary of the current status:

### What Works:
- **Basic GUI**: A graphical user interface (GUI) has been implemented using `wxPython`.
- **CSV Import**: Students can be imported from a CSV file with customizable delimiter and header settings.
- **Randomization**: Students are randomly shuffled, which is a foundational step for group creation.

### What’s Not Working:
- **Group Creation**: The group creation logic is partially implemented but does not yet produce the expected results. Groups are not being correctly formed or displayed.
- **Error Handling**: The application lacks robust error handling, especially for edge cases like invalid group sizes or CSV files.
- **Testing**: Comprehensive unit tests are missing, making it difficult to identify and fix issues.

### What’s Missing:
- **Advanced Grouping Logic**: Additional logic to ensure fair and non-repeating student pairings across multiple rounds.

---

## How to Use

### Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.10 or higher
- `uv` (a fast Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DrKnallfrosch/wxCreateGroups.git