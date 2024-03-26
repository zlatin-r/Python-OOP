from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Hero", 1, 100.00, 100.00)
        self.enemy = Hero("enemy", 1, 50, 50.00)

    def test_init(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100.00, self.hero.health)
        self.assertEqual(100.00, self.hero.damage)

    def test_battle_hero_whit_himself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_enemy_hero_health_is_zero_raises_exception(self):
        self.enemy.health = 0
        expected_string = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_string, str(ex.exception))

    def test_battle_hero_with_zero_health_raises_exception(self):
        self.hero.health = 0
        expected_massage = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_massage, str(ex.exception))

    def test_battle_with_draw_result_returns_draw_and_decreases_both_heroes_health(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_battle_hero_wins_and_increases_level_health_damage_returns_correct_string(self):
        expected_string = "You win"
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_string, result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle_hero_lost_enemy_increases_level_health_damage(self):
        pass


if __name__ == '__main__':
    main()
