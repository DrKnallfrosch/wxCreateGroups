from abc import ABC, abstractmethod


class GroupInterface(ABC):
    """
    Reset a group to its initial state.

    :return: None
    """
    @abstractmethod
    def reset_group(self):
        """
        Reset a group to its initial state.

        :return: None
        """
        pass

    @abstractmethod
    def create_groups(self):
        """
        Create groups.

        :return: None
        """
        pass

    @abstractmethod
    def visualise_groups(self) -> dict[int, dict[str, list[str]]]:
        """
        :return: A dictionary containing groups, where the key is an integer representing the group ID and the value
        is another dictionary. This nested dictionary has the structure where the key is a string representing the
        group property and the value is a list of strings representing the members of that group.
        """
        pass

    @abstractmethod
    def get_current_groups(self) -> dict[int, dict[str, list[str]]]:
        """
        :return: A dictionary containing information about the current groups.
            The dictionary keys are integers representing group IDs.
            The corresponding values are dictionaries with string keys (group information)
            and lists of strings (group members).
        """
        pass

    @abstractmethod
    def get_all_groups(self) -> dict[int, dict[str, list[str]]]:
        """

        :return: a dictionary mapping group IDs to dictionaries containing group information. Each group information
        dictionary contains a 'name' key which holds the group name (str) and a 'members' key which holds a list of
        member names (list[str]).

        """
        pass

    @abstractmethod
    def select_from_file(self):
        """
        Method for selecting a file.

        :return: None

        """
        pass

    @abstractmethod
    def can_repeat(self) -> int:
        pass
