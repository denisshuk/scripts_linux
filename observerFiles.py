#import os
import asyncio
from watchfiles import awatch

#dirDestination = ''
#dirSource = ':'

async def main():
    test = awatch("./")
    async for changes in test:
        if (list(changes)[0][0] == 1):
#            os.system(f'rsync -a {list(changes)[0][1]} ./test.d/')
            print('create')
        if (list(changes)[0][0] == 2):
            print ("mod")
        if (list(changes)[0][0] == 3):
            print ("del")

asyncio.run(main())
