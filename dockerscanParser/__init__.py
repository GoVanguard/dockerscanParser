class DockerscanParser:
    def __init__(self):
        pass

    def openFile(self, inputFileName):
        fileObj = open(inputFileName, 'r')
        fileData = fileObj.readlines()
        return fileData

    def stripTrash(self, inputText):
        inputText = inputText.replace("',", "")
        inputText = inputText.replace(" '", "")
        inputText = inputText.replace("#", "")
        inputText = inputText.replace("[]", "")
        inputText = inputText.replace("- ", "")
        inputText = inputText.replace("Dockscan Report", "")
        inputText = inputText.replace("  ", "")
        return inputText

    def cleanResults(self, inputText):
        currentIssueStr =  ' '.join(inputText)
        currentIssueStr =  "{" + currentIssueStr
        currentIssueStr =  currentIssueStr.replace("Description: ", "'Description': '")
        currentIssueStr =  currentIssueStr.replace(" Output: ", "', 'Output': '")
        currentIssueStr =  currentIssueStr.replace(" Solution: ", "', 'Solution': '")
        currentIssueStr =  currentIssueStr.replace("']\"]", "")
        currentIssueStr =  currentIssueStr.replace(" ']", "")
        currentIssueStr =  currentIssueStr + "'}"
        currentIssueStr =  currentIssueStr.replace(" '", "'")
        currentIssueStr =  currentIssueStr.replace("  '", "'")
        return currentIssueStr

    def splitDataFromDockerscan(self, inputCleanData):
        import re
        results = {}
        currentGroup = None
        lastGroup = None
        currentIssue = None
        currentIssueData = []
        for keyEntry in inputCleanData:
            groupSearch = re.search(r'\-\[ (.*?) \]\-', keyEntry)
            issueSearch = re.search(r'=(.*?)=', keyEntry)
            if groupSearch:
                currentGroup = groupSearch.group(1)
                results[currentGroup] = {}
            elif issueSearch:
                if currentIssueData != [] and str(currentIssueData) != '[\'["[\\\'\', \'\']' and str(currentIssueData) != '["[\'", \'\']':
                    results[lastGroup][currentIssue] = eval(self.cleanResults(currentIssueData))
                currentIssue = issueSearch.group(1)
                results[currentGroup][currentIssue] = {}
                lastGroup = currentGroup
                currentIssueData = []
            else:
                currentIssueData.append(keyEntry)
        results[lastGroup][currentIssue] = eval(self.cleanResults(currentIssueData))
        return results

    def parseReport(self, reportFileName):
        fileData = self.openFile(reportFileName)
        inputCleanText = self.stripTrash(str(fileData))
        inputCleanData = inputCleanText.split('\\n')
        issueResults = self.splitDataFromDockerscan(inputCleanData)
        return issueResults

def test():
    dp = DockerscanParser()
    results = dp.parseReport('dockerscan.txt')
    print(results)
