import unittest
from Quarto import Game

# test_Quarto.py

class TestGame(unittest.TestCase):
    def setUp(self):
        """Création d'une nouvelle partie"""
        self.game = Game()
        self.game.Pions = {
            "SLEP", "SDEP", "SLEC", "BDEC", "SLFP", "SLFC",
            "BDFP", "SDFP", "SDFC", "BLFP", "SDEC", "BLEP",
            "BDEP", "BLFC", "BLEC", "BDFC"
        }

    #@unittest.timeout(5) # Timeout pour etviter boucle infinie

    def test_run_with_empty_board(self): #Test et lance la méthode run avec un plateau vide
       
        self.game.plateau = [None, None, None, None, None, None, None, None,
                            None, None, None, None, None, None, None, None] 
        self.game.piece_a_jouer = "SLEP"
        self.game.run()
        self.assertIsNotNone(self.game.jeu["pos"], "Position doit être mise")
        self.assertIn(self.game.jeu["piece"], self.game.Pions, "Pièce doit être valide")

    def test_run_with_almost_winning_board(self): # Test et lance la méthode run avec un plateau presque gagnant
        
        self.game.plateau = ["SLEP", "SDEP", "SLEC", None] + [None] * 12
        self.game.piece_a_jouer = "BDEC"
        self.game.run()
        self.assertEqual(self.game.jeu["pos"], 3, "Devrait placer la pièce à la bonne position")
        self.assertIn(self.game.jeu["piece"], self.game.Pions, "Pièce doit être valide")

    def test_run_with_no_piece_to_play(self): # Test et lance méthode run sans pièce à jouer
        
        self.game.plateau = [None, None, None, None, None, None, None, None,
                            None, None, None, None, None, None, None, None]
        self.game.piece_a_jouer = None
        self.game.run()
        self.assertIsNotNone(self.game.jeu["piece"], "Une pièce devrait être sélectionnée")
        self.assertIn(self.game.jeu["piece"], self.game.Pions, "Pièce doit être valide")

if __name__ == "__main__":
    unittest.main()