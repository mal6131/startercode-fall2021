from mrjob.job import MRJob

class wordCount(MRJob):
    def mapper_init(self):
        self.cache = {}
        self.letter = {}
        self.lines = {'_lines_': 0}

    def mapper(self, key, line):
        #line = re.sub(r'[^\w\s]', '', line)
        words = line.split()
        symbols = list(line)
        for w in words:
            if w in self.cache:
                self.cache[w] += 1
                limit = 150
                if (len(self.cache) > limit):
                    for x in self.cache:
                        yield ("_"+x, self.cache[x])
                    self.cache.clear()
            else:
                self.cache[w] = 1
        for s in symbols:
            if s.isalpha():
                if s in self.letter:
                    self.letter[s] += 1
                else:
                    self.letter[s] = 1
            self.lines['_lines_'] += 1

    def mapper_final(self):
        if len(self.cache) != 0:
            for x in self.cache:
                yield ("_"+x, self.cache[x])
        for s in self.letter:
            yield(s+"_", self.letter[s])
        yield ('_lines_', self.lines['_lines_'])

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    wordCount.run()