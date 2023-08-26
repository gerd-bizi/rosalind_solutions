class Solution:
    def strings_and_lists(s, i, j, k, l):
        return s[i:j+1] + " " + s[k:l+1]

    if __name__ == "__main__":
        print(strings_and_lists(
            "zgbssLmC1TlcdTk3WJLJNlg9SEsvUOKGb6ipOCa1YPtHSc38mEeFkiofc6KfCervus8rNZGsfeiQt1QK2XgqXLBxxGxbd3EiUrKco3l6REh5pKBwaGalbigular2eKze8m6H1n4GsTc7qeM9UrR2oQXga8QFHGL6YtKNBIBXPjU3JF879xR7bRKfqG5oTIChGGnrqS.",
            60, 65, 114, 121
        ))