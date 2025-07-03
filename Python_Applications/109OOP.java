class Arithmatic
{
    public int no1, no2;

    public Arithmatic(int A, int B)
    {
        this.no1 = A;
        this.no2 = B;
    }

    public int Addition()
    {
        int result = 0;
        result = this.no1 + this.no2;
        return result;
    }
}

class ObjectOriented
{
    public static void main(String A[])
    {
        Arithmatic obj = new Arithmatic(10, 11);

        int ret = 0;
        ret = obj.Addition();
        System.out.println("Addition is : "+ ret);
    }
}