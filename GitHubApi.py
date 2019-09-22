'''
Created on Sep 22, 2019

@author: Christian Smith
'''
import unittest
from github import Github

def getRepositories(user_id):
    if(' ' in user_id or len(user_id) == 0):
        print(user_id + ' is an invalid username')
        return 'invalid'
    else:
        g = Github("f26a21eb3a5288199012753649a52a9b5bed8bc9")
        print('User: ' + user_id)
        user = g.get_user(user_id)
        for repo in user.get_repos():
            try:
                print('Repo: ' + repo.name + ' Number of commits: ' + str(repo.get_commits().totalCount))
            except:
                print('EMPTY REPO')
    return 'valid'
            
    
class Test(unittest.TestCase):
    
    def testInvalid(self):
        self.assertIs(getRepositories('j24 12'), 'invalid', 'User ID with spaces is invalid')
        self.assertIs(getRepositories(''), 'invalid', 'Empty User ID is invalid')
        
    def testValid(self):
        self.assertIs(getRepositories('Dioden'), 'valid', 'User ID should be valid')
        self.assertIs(getRepositories('google'), 'valid', 'User ID should be valid')
        self.assertIs(getRepositories('amzn'), 'valid', 'User ID should be valid')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    g = Github("f26a21eb3a5288199012753649a52a9b5bed8bc9")
    unittest.main(exit = False)
