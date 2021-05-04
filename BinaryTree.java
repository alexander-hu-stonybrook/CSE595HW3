import java.util.*;

class BinaryTree<T> implements Iterable<T>{

    private T data;
    private BinaryTree<T> LTree = null;
    private BinaryTree<T> RTree = null;

    public BinaryTree() {
        this.data = null;
    }

    public BinaryTree(T firstvalue) {
        this.data = firstvalue;
    }

    public T getData() {
        return this.data;
    }

    public void setData(T newvalue) {
        this.data = newvalue;
    }

    public BinaryTree<T> getLeftChild() {
        return this.LTree;
    }

    public BinaryTree<T> getRightChild() {
        return this.RTree;
    }

    public void addLeftChild(BinaryTree<T> newtree) {
        this.LTree = newtree;
    }

    public void addRightChild(BinaryTree<T> newtree) {
        this.RTree = newtree;
    }

    @Override
    public Iterator<T> iterator() {
        return new BinaryTreeIterator<T>(this);
    }

    class BinaryTreeIterator<T> implements Iterator<T>{

        List<BinaryTree<T>> queuelist = new ArrayList<BinaryTree<T>>();
        BinaryTree<T> cursor;

        public BinaryTreeIterator(BinaryTree<T> intree) {
            this.cursor = intree;
            if (this.cursor.getData() != null) {
                queuelist.add(this.cursor);
            }
        }

        public boolean hasNext() {

            if (queuelist.size() == 0) {
                return false;
            }
            return true;
        }

        //Need to think about what T type really should be
        public T next() {
            this.cursor = queuelist.remove(0);

            if (this.cursor.getLeftChild() != null) {
                if (this.cursor.getLeftChild().getData() != null) {
                    queuelist.add(this.cursor.getLeftChild());
                }
            }
            if (this.cursor.getRightChild() != null) {
                if (this.cursor.getRightChild().getData() != null) {
                    queuelist.add(this.cursor.getRightChild());
                }
            }

            return cursor.getData();
        }

    }

    @Override
    public String toString() {
        return (this.data).toString();
    }
}