import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.*;

public class ProducerConsumer {
    private static final int BUFFER_SIZE = 10;
    private static final Queue<Integer> buffer = new LinkedList<>();
    private static final Lock lock = new ReentrantLock();
    private static final Condition notFull = lock.newCondition();
    private static final Condition notEmpty = lock.newCondition();
    private static final int LIMIT = 5;

    public static void main(String[] args) {
        Thread producerThread = new Thread(new Producer(LIMIT));
        Thread consumerThread = new Thread(new Consumer(LIMIT));

        producerThread.start();
        consumerThread.start();
    }

    static class Producer implements Runnable {
        private int limit;

        public Producer(int limit) {
            this.limit = limit;
        }

        @Override
        public void run() {
            try {
                for (int i = 0; i < limit; i++) {
                    int item = produceItem();
                    lock.lock();
                    try {
                        while (buffer.size() == BUFFER_SIZE) {
                            notFull.await();
                        }
                        buffer.add(item);
                        System.out.println("Produced: " + item);
                        notEmpty.signal();
                    } finally {
                        lock.unlock();
                    }
                    // Adding a delay to simulate time taken for producing an item
                    Thread.sleep(100); // Delay of 100 milliseconds
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        private int produceItem() {
            return (int) (Math.random() * 100);
        }
    }

    static class Consumer implements Runnable {
        private int limit;

        public Consumer(int limit) {
            this.limit = limit;
        }

        @Override
        public void run() {
            try {
                for (int i = 0; i < limit; i++) {
                    lock.lock();
                    try {
                        while (buffer.isEmpty()) {
                            notEmpty.await();
                        }
                        int item = buffer.poll();
                        System.out.println("Consumed: " + item);
                        notFull.signal();
                    } finally {
                        lock.unlock();
                    }
                    // Adding a delay to simulate time taken for consuming an item
                    Thread.sleep(150); // Delay of 150 milliseconds
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
