from abc import ABC, abstractmethod
from GroupCalculator import Student


class GroupInterface(ABC):
    """
    An abstract base class that defines the interface for group operations.
    This interface ensures that any class implementing it provides methods for managing,
    creating, visualizing, and retrieving groups.
    """

    @abstractmethod
    def reset_group(self) -> None:
        """
        Resets all group assignments to their initial state.

        This method should clear any existing groups and prepare the system for a fresh group generation.

        :return: None
        """
        pass

    @abstractmethod
    def create_groups(self) -> None:
        """
        Creates a new set of groups based on predefined rules.

        The implementation should ensure a fair distribution of members and avoid repetition in consecutive rounds.

        :return: None
        """
        pass

    @abstractmethod
    def visualise_groups(self) -> dict[int, dict[str, list[Student]]]:
        """
        Returns a dictionary representing the currently generated groups.

        The dictionary structure is as follows:
        - The key (int) represents the round number.
        - The value (dict) maps group labels (str) to a list of member names (list[str]).

        :return: A dictionary containing the visual representation of the groups.
        :rtype: dict[int, dict[str, list[str]]]
        """
        pass

    @abstractmethod
    def get_current_groups(self) -> dict[int, dict[str, list[Student]]]:
        """
        Retrieves the groups from the most recent round.

        The dictionary structure is:
        - The key (int) represents the round number.
        - The value (dict) maps group labels (str) to a list of member names (list[str]).

        :return: A dictionary containing the latest group allocations.
        :rtype: dict[int, dict[str, list[str]]]
        """
        pass

    @abstractmethod
    def get_all_groups(self) -> dict[int, dict[str, list[Student]]]:
        """
        Retrieves all previously created group assignments.

        The dictionary structure is:
        - The key (int) represents the round number.
        - The value (dict) maps group labels (str) to a list of member names (list[str]).

        :return: A dictionary containing all generated group assignments across multiple rounds.
        :rtype: dict[int, dict[str, list[str]]]
        """
        pass

    @abstractmethod
    def select_from_file(self, file_path: str) -> None:
        """
        Allows the user to select a file containing participant data.

        The implementation should read the file, extract relevant information, and prepare it for group generation.

        :return: None
        """
        pass

    @abstractmethod
    def can_repeat(self) -> int:
        """
        Determines the maximum number of unique group combinations possible.

        This method should calculate how many distinct group assignments can be made before repetition occurs.

        :return: The maximum number of unique groupings (int).
        :rtype: int
        """
        pass
