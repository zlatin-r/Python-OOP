from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args: Player):
        added_players = []

        for player in args:
            if not self._check_if_player_is_already_added(player):
                added_players.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args: Supply):
        for sup in args:
            self.supplies.append(sup)

    def sustain(self, player_name: str, sustenance_type: str):
        valid_sustenance_types = ["Food", "Drink"]
        if self._find_player_by_name(player_name):
            if sustenance_type in valid_sustenance_types:
                sustenance = self._check_if_have_sustenance(sustenance_type)
                player = self._find_player_by_name(player_name)

                if not player.need_sustenance:
                    return f"{player_name} have enough stamina."

                player.stamina = min(player.stamina + sustenance.energy, 100)
                return f"{player_name} sustained successfully with {sustenance.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self._find_player_by_name(first_player_name)
        player2 = self._find_player_by_name(second_player_name)

        if player1.stamina == 0 and player2.stamina == 0:
            return (f"Player {player1.name} does not have enough stamina.\n"
                    f"Player {player2.name} does not have enough stamina.")

        for player in (player1, player2):
            if player.stamina == 0:
                return f"Player {player.name} does not have enough stamina."

        attacker, defender = self._first_attacker_defender(player1, player2)

        winner = self._attack(attacker, defender)
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            self._reduce_stamina(player)
            self.sustain(player, "Food")
            self.sustain(player, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))

        for sustenance in self.supplies:
            result.append(sustenance.details())

        return "\n".join(result)



    # Helping methods:

    def _check_if_player_is_already_added(self, player: Player):
        result = next(filter(lambda p: p.name == player.name, self.players), None)
        return result

    def _find_player_by_name(self, player_name: str):
        result = next(filter(lambda p: p.name == player_name, self.players), None)
        return result

    def _check_if_have_sustenance(self, sustenance_type: str):
        result = next(filter(lambda s: type(s).__name__ == sustenance_type, self.supplies[::-1]), None)
        # TODO CHECK IF RETURNS THE LAST ADDED SUPPLY FROM THIS TYPE
        if result:
            self.supplies.remove(result)
            # TODO CHECK IF IS REMOVED FROM SUPPLYS LIST
            return result
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def _first_attacker_defender(self, player1: Player, player2: Player):
        if player1.stamina < player2.stamina:
            return player1, player2
        elif player2.stamina < player1.stamina:
            return player2, player1

    def _attack(self, attacker: Player, defender: Player):

        defender.stamina -= attacker.stamina / 2
        if defender.stamina <= 0:
            defender.stamina = 0
            return attacker

        attacker.stamina -= defender.stamina / 2
        if attacker.stamina <= 0:
            attacker.stamina = 0
            return defender

        if attacker.stamina > defender.stamina:
            return attacker
        elif defender.stamina > attacker.stamina:
            return defender

    def _reduce_stamina(self, player: Player):
        player.stamina = max(player.stamina - player.age * 2, 0)

