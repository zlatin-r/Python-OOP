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

    def test_battle_username_and_enemy_name_are_same_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_enemy_hero_health_is_zero_raises_exception(self):
        self.enemy.health = 0
        expected_string = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_string, str(ex.exception))

    def test_battle_with_zero_health_raises_exception(self):
        self.hero.health = 0
        expected_massage = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_massage, str(ex.exception))

    def test_battle_with_draw_result_returns_draw_and_decrease_health(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual()

if __name__ == '__main__':
    main()
