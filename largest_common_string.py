def largest_common_substring(s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        p = ''
        for i in range(n):
        	p = p + s[n - i - 1]
        lcSuff = [[0 for i in range(n)] for j in range(n)]
    	

        for i in range(0, n):
        	for j in range(0, n):
        		print i
        		print j
        		if s[i] == p[j]:
        			print i
        			print j
        			if i == 0 or j == 0:
        				lcSuff[i][j] = 1
        			else:
        				lcSuff[i][j] = lcSuff[i - 1][j - 1] + 1
        		else:
        			lcSuff[i][j] = 0
        max_com_substring = lcSuff[0][0]
        first_last_com = 0
        second_last_com = 0
        for i in range(n):
        	for j in range(n):
        		if lcSuff[i][j] > max_com_substring:
        			max_com_substring = lcSuff[i][j]
        			first_last_com = i
        			second_last_com = j

        return s[first_last_com - max_com_substring + 1: first_last_com + 1]


