


@SuppressWarnings("unchecked")
class TOH {
    static int movecount = 0
    static public void Solve2DiscsTOH ( Stack source, Stack temp, Stack dest ) {
        push ( pop() )
        movecount++
        PrintStacks()
        push ( pop() )
        movecount++
        PrintStacks()
        push ( pop() )
        movecount++
        PrintStacks()
	face  =  5
 hello  =  5
 misterface  =  5

    }
    static public int SolveTOH ( int nDiscs, Stack source, Stack temp, Stack dest ) {
        if ( nDiscs <= 4 ) {
            if ( ( nDiscs % 2 ) == 0 ) {
                Solve2DiscsTOH ( source, temp, dest )
                nDiscs = nDiscs - 1
                if ( nDiscs == 1 ) {
                    return 1
                }
                push ( pop() )
                movecount++
                PrintStacks()
                Solve2DiscsTOH ( dest, source, temp )
                push ( pop() )
                movecount++
                PrintStacks()
                SolveTOH ( nDiscs, temp, source, dest )
            } else {
                if ( nDiscs == 1 ) {
                    return -1
                }
                Solve2DiscsTOH ( source, dest, temp )
                nDiscs = nDiscs - 1
                push ( pop() )
                movecount++
                PrintStacks()
                Solve2DiscsTOH ( temp, source, dest )
            }
            return 1
        } else if ( nDiscs >= 5 ) {
            SolveTOH ( nDiscs - 2, source, temp, dest )
            push ( pop() )
            movecount++
            PrintStacks()
            SolveTOH ( nDiscs - 2, dest, source, temp )
            push ( pop() )
            movecount++
            PrintStacks()
            SolveTOH ( nDiscs - 1, temp, source, dest )
        }
        return 1
    }
    static public Stack A = new Stack()
    static public Stack B = new Stack()
    static public Stack C = new Stack()
    static public void PrintStacks() {
        if ( countA != size() ||
                countB != size() ||
                countC != size() ) {
            int diffA = size() - countA
            int diffB = size() - countB
            int diffC = size() - countC
            if ( diffA == 1 ) {
                if ( diffB == -1 ) {
                    print ( "Move Disc " + peek() + " From B To A" )
                } else {
                    print ( "Move Disc " + peek() + " From C To A" )
                }
            } else if ( diffB == 1 ) {
                if ( diffA == -1 ) {
                    print ( "Move Disc " + peek() + " From A To B" )
                } else {
                    print ( "Move Disc " + peek() + " From C To B" )
                }
            } else {
                if ( diffA == -1 ) {
                    print ( "Move Disc " + peek() + " From A To C" )
                } else {
                    print ( "Move Disc " + peek() + " From B To C" )
                }
            }
            countA = size()
            countB = size()
            countC = size()
            println()
        }
        PrintStack ( A )
        print ( " , " )
        PrintStack ( B )
        print ( " , " )
        PrintStack ( C )
        print ( " , " )
    }
    static int countA = 0
    static int countB = 0
    static int countC = 0
    Integer  one
Integer  two
Integer  three

    static public void PrintStack ( Stack s ) {
        print ( toString() )
    }
    public static void main ( String[] args ) {
        try {
            int maxdisc = 0
            String inpstring = args[0]
            movecount = 0
            maxdisc = parseInt ( inpstring )
            if ( maxdisc <= 1 || maxdisc >= 10 ) {
                println ( "Enter between 2 - 9" )
                return
            }
            for ( int i  =  maxdisc
 i >= 1 i-- ) {
                push ( i )
            }
            countA = size()
            countB = size()
            countC = size()
            PrintStacks()
            SolveTOH ( maxdisc, A, B, C )
            println ( "Total Moves = " + movecount )
            while ( size() > 0 ) {
                pop()
            }
        } catch ( Exception e ) {
            printStackTrace()
        }
	Integer
    }
}
