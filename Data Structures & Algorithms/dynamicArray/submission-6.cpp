class DynamicArray {
private:
    int *A;
    int capacity;
    int len;
public:

    DynamicArray(int capacity) {
        A = new int[capacity];
        len = 0;
        this->capacity=capacity;
    }

    int get(int i) {
        if (i>=0 && i<=this->capacity-1)
            return A[i];
        return -1;
    }

    void set(int i, int n) {
        if (i>=0 && i<=this->capacity-1)
            A[i]=n;
    }

    void pushback(int n) {
        if (len==this->capacity)
            resize();
        A[len++]=n;
    }

    int popback() {
        if (len>0){
            len--;
            return A[len];
            }
        return -1;
    }

    void resize() {
        int *ptr = new int[this->capacity*2];
        for (int i = 0;i<this->capacity ;i++){
            ptr[i]=A[i];
        }
        this->capacity=capacity*2;
        delete []A;
        A = ptr;
    }

    int getSize() {
        return len;
    }

    int getCapacity() {
        return this->capacity;
    }
};
