class Solution(object):
    def compress(self, chars):

        read = 0
        write = 0

        while read < len(chars):

            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for s in str(count):
                    chars[write] = s
                    write += 1

        return write