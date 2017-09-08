# -*- coding: utf-8 -*-

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def equal_score_less_than_three(self, p1points, p2points):
        result = ""
        if (p1points == p2points and p1points < 3):
            if (p1points==0):
                result = "Love"
            if (p1points==1):
                result = "Fifteen"
            if (p1points==2):
                result = "Thirty"
            result += "-All"
        if (p1points==p2points and p1points>2):
            result = "Deuce"
        return result

    def score(self):
        result = self.equal_score_less_than_three(self.p1points, self.p2points)

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = "Fifteen"
            if (self.p1points==2):
                P1res = "Thirty"
            if (self.p1points==3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = "Fifteen"
            if (self.p2points==2):
                P2res = "Thirty"
            if (self.p2points==3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res


        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res="Thirty"
            if (self.p1points==3):
                P1res="Forty"
            if (self.p2points==1):
                P2res="Fifteen"
            if (self.p2points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res="Thirty"
            if (self.p2points==3):
                P2res="Forty"
            if (self.p1points==1):
                P1res="Fifteen"
            if (self.p1points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res


        result = self.advantage_for(self.p1points, self.p2points, self.player1Name, result)
        result = self.advantage_for(self.p2points, self.p1points, self.player2Name, result)
        result = self.win_for(self.p1points, self.p2points, self.player1Name, result)
        result = self.win_for(self.p2points, self.p1points, self.player2Name, result)
        return result

    def win_for(self, player_points, other_player_points, player_name, result):
        if (player_points >= 4 and other_player_points >= 0 and (player_points-other_player_points) >= 2):
            result = "Win for " + player_name
        return result

    def advantage_for(self, player_points, other_player_points, player_name, result):
        if (player_points > other_player_points and other_player_points >= 3):
            result = "Advantage " + player_name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points +=1


    def P2Score(self):
        self.p2points +=1
