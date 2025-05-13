import unittest
from Quarto import Game

# test_Quarto.py

class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up a new Game instance for each test."""
        self.game = Game()
        self.game.Pions = {
            "SLEP", "SDEP", "SLEC", "BDEC", "SLFP", "SLFC",
            "BDFP", "SDFP", "SDFC", "BLFP", "SDEC", "BLEP",
            "BDEP", "BLFC", "BLEC", "BDFC"
        }

    def test_run_with_empty_board(self):
        """Test the run method with an empty board."""
        self.game.plateau = [None] * 16
        self.game.piece_a_jouer = "SLEP"
        self.game.run()
        self.assertIsNotNone(self.game.jeu["pos"], "Position should be set.")
        self.assertIn(self.game.jeu["piece"], self.game.Pions, "Piece should be valid.")

    def test_run_with_almost_winning_board(self):
        """Test the run method with a nearly winning board."""
        self.game.plateau = ["SLEP", "SDEP", "SLEC", None] + [None] * 12
        self.game.piece_a_jouer = "BDEC"
        self.game.run()
        self.assertEqual(self.game.jeu["pos"], 3, "Should place the piece in the winning position.")
        self.assertIn(self.game.jeu["piece"], self.game.Pions, "Piece should be valid.")

    def test_run_with_no_piece_to_play(self):
        """Test the run method when no piece is provided."""
        self.game.plateau = [None] * 16
        self.game.piece_a_jouer = None
        self.game.run()
        self.assertIsNotNone(self.game.jeu["piece"], "A piece should be selected.")
        self.assertIn(self.game.jeu["piece"], self.game.Pions, "Piece should be valid.")

if __name__ == "__main__":
    unittest.main()
