import java.util.concurrent.*;

public class ProducerConsumer {
    private static BlockingQueue<Integer> Buffer = new LinkedBlockingDeque<>();
    private static Semaphore emptySlots = new Semaphore(10);
    private static Semaphore fullSlots = new Semaphore(0);
    private static final int LIMIT = 5;  // Set the limit for producer and consumer

    public static void main(String args[]) {
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
                    emptySlots.acquire(); // Wait until there's an empty slot
                    Buffer.put(item); // Add the item to the buffer
                    System.out.println("Produced: " + item);
                    fullSlots.release(); // Signal that there's a full slot
                    Thread.sleep(100); // Delay to simulate production time
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
                    fullSlots.acquire(); // Wait until there's a full slot
                    int item = Buffer.take(); // Remove the item from the buffer
                    System.out.println("Consumed: " + item);
                    emptySlots.release(); // Signal that there's an empty slot
                    Thread.sleep(150); // Delay to simulate consumption time
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
