from collections import Counter, namedtuple
import heapq

class Image:

    def __init__(self, filename):
        with open(filename, 'r') as f:
            img = f.read()
            rows = img.split('\n')
            rows.pop()
            self.pixels = []
            self.type = rows.pop(0)
            self.width = int(rows[0].split(' ')[0])
            self.height = int(rows[0].split(' ')[1])
            rows.pop(0)
            self.smth = rows[0]
            rows.pop(0)
            self.get_pixels(rows)
            self.compressor = Compressor()


    def get_pixels(self, rows):
        self.pixels = []
        if self.type=='P2':
            for i in rows:
                current_row = i.split(' ')
                if current_row[len(current_row)-1] == '':
                    current_row.pop()
                self.pixels.append([int(element) for element in current_row])

        if self.type == 'P3':
            for i in rows:
                current_row = i.split(' ')
                self.pixels.append([int(element) for element in current_row])


    def save_image(self, filename):
        with open (filename, 'w') as f:
            if self.type == 'P2':
                f.write('P2\n')
                f.write(str(self.width) + ' ' + str(self.height) + "\n")
                f.write(str(255) + "\n")
                for i in self.pixels:
                    for j in i:
                        f.write(str(j) + " ")
                    f.write("\n")

    def rle(self):
        if self.type == 'P2' or self.type == 'P3':
            return self.compressor.rle(self.pixels)

    def huffman(self):
        if self.type == 'P2' or self.type == 'P3':
            return self.compressor.huffman(self.pixels)


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf (namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc


class Compressor:

    def __init__(self):
        pass

    def rle(self, pixels):
        res = []
        prev = ''
        count = 1
        for i in pixels:
            for j in i:
                if prev == '':
                    prev = j
                elif prev == j:
                    count += 1
                else:
                    res.append((prev, count))
                    prev = j
                    count = 1
        if count != 1:
            res.append((prev, count))
        return res

    def huffman(self, pixels):
        string = []
        for i in pixels:
            for j in i:
                string.append(j)
        h = []
        for ch, freq in Counter(string).items():
            h.append((freq, len(h), Leaf(ch)))
        heapq.heapify(h)
        count = 0
        while len(h) > 1:
            freq1, _count1, left = heapq.heappop(h)
            freq2, _count2, right = heapq.heappop(h)
            heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
            count += 1

        [(_freq, _count, root)] = h
        code = {}
        root.walk(code, "")
        return "".join(code[ch] for ch in string)

    def lz77(self, pixels):
        res = []
        buffer = 10
        string = []
        for i in pixels:
            for j in i:
                string.append(j)
        max_len = len(string)
        for i in range(max_len):
            pass
        return res