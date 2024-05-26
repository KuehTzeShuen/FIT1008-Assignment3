from landsites import Land


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = sites
        self.adventurers = adventurers


    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        # Calculate the value of each site as the ratio of gold to guardians
        for site in self.sites:
            site.value = site.gold / site.guardians

        # Sort the sites by value in descending order
        temp_sites = self.sites.copy()
        temp_sites.sort(key=lambda site: site.value, reverse=True)
        
        temp_adventurers = self.adventurers

        selected_sites = []
        for site in temp_sites:
            if temp_adventurers == 0:
                break

            # Send as many adventurers as possible to the site
            adventurers_to_send = min(temp_adventurers, site.guardians)
            selected_sites.append((site, adventurers_to_send))

            # Update the number of available adventurers
            temp_adventurers -= adventurers_to_send

        return selected_sites

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        rewards = []
        for adventurers in adventure_numbers:
            # Calculate the value of each site as the ratio of gold to guardians
            for site in self.sites:
                site.value = site.gold / site.guardians

            # Sort the sites by value in descending order
            temp_sites = self.sites.copy()
            temp_sites.sort(key=lambda site: site.value, reverse=True)

            total_reward = 0
            for site in temp_sites:
                if adventurers == 0:
                    break

                # Send as many adventurers as possible to the site
                adventurers_to_send = min(adventurers, site.guardians)
                # Adjust the reward based on the actual number of guardians that can be defeated
                # reward = adventurers_to_send * site.gold / max(adventurers, site.guardians)
                reward = min(site.get_gold() * adventurers_to_send / site.get_guardians(), site.get_gold())
                total_reward += reward

                # Update the number of available adventurers
                adventurers -= adventurers_to_send

            rewards.append(total_reward)

        return rewards

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        land.gold = new_reward
        land.guardians = new_guardians
        print("updated", land.gold, land.guardians)
