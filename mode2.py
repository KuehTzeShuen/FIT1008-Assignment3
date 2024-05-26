from landsites import Land


class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, n_teams: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        
        self.number_of_adventurer_teams = n_teams
        self.sites = []

    def add_sites(self, sites: list[Land]) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        for i in sites:
            if i not in self.sites:
                self.sites.append(i)
        print(self.sites)

    # def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
    #     """
    #     Student-TODO: Best/Worst Case
    #     """
    #     selected_sites = []
    #     for _ in range(self.number_of_adventurer_teams):
    #         # Sort the sites by gold in descending order
    #         self.sites.sort(key=lambda site: site.gold, reverse=True)

    #         temp_adventurers = adventurer_size
    #         for site in self.sites:
    #             if temp_adventurers == 0:
    #                 break

    #             # Send as many adventurers as possible to the site
    #             adventurers_to_send = min(temp_adventurers, site.guardians)
    #             # Calculate the gold made by the team
    #             gold_made = min(site.get_gold() * adventurers_to_send / site.get_guardians(), site.get_gold())
    #             # Calculate the final score
    #             final_score = gold_made + (adventurer_size - adventurers_to_send) * 2.5
    #             selected_sites.append((site, adventurers_to_send, final_score))

    #             # Update the number of available adventurers
    #             temp_adventurers -= adventurers_to_send

    #             # Update the site's state
    #             site.gold -= gold_made
    #             site.guardians -= adventurers_to_send

    #     return selected_sites

    # Step 1: Implement compute_score method
    def compute_score(self, site, adventurer_size):
        # Calculate the maximum score, remaining adventurers, and gold gained
        adventurers_to_send = min(adventurer_size, site.guardians)
        gold_made = min(site.get_gold() * adventurers_to_send / site.get_guardians(), site.get_gold())
        final_score = gold_made + (adventurer_size - adventurers_to_send) * 2.5
        remaining_adventurers = adventurer_size - adventurers_to_send
        return final_score, remaining_adventurers, gold_made

    # Step 2: Implement construct_score_data_structure method
    def construct_score_data_structure(self, adventurer_size):
        # Create a heap to store the scores of the sites
        scores_heap = []
        for site in self.sites:
            score, remaining_adventurers, gold_made = self.compute_score(site, adventurer_size)
            # Add the score and site to the heap
            heapq.heappush(scores_heap, (-score, site))
        return scores_heap

    # Step 3: Modify simulate_day method
    def simulate_day(self, adventurer_size):
        # Construct the scores heap
        scores_heap = self.construct_score_data_structure(adventurer_size)
        selected_sites = []
        for _ in range(self.number_of_adventurer_teams):
            # Get the site with the highest score
            score, site = heapq.heappop(scores_heap)
            # Send adventurers to the site and update its state
            adventurers_to_send = min(adventurer_size, site.guardians)
            site.gold -= gold_made
            site.guardians -= adventurers_to_send
            selected_sites.append((site, adventurers_to_send, -score))
        return selected_sites