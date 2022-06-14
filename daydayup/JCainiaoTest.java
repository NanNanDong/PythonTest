import java.lang.reflect.Field;
import java.security.KeyStore.Entry;
import java.util.HashMap;
import java.util.Objects;

public class JCainiaoTest {

    public static void main(String[] args) {
        Student stu1 = new Student("haha",10);
        Student stu2 = new Student("haha",10);

        boolean result1 = isDeepEquals(stu1, stu2);
        boolean result2 = Objects.deepEquals(stu1, stu2);
        System.out.println(result1 + "," + result2);
    }

    public class Student {
        String name;
        int age;

        public Student(String name, int age){
            this.name = name;
            this.age = age;
        }

    }


    public static boolean isDeepEquals(Object src, Object dst) {

        if (src == dst)
            return true;
        
        if (src == null || dst == null)
            return false;
        
        // 职责划分上，hashcode应该由业务实现，反射去获取字段，有潜在性能隐患
        // return src.hashCode() == dst.hashCode();
        Class<?> clzSrc = src.getClass();
        Class<?> clzDst = dst.getClass();
        // 类型不同
        if (!clzSrc.equals(clzDst))
            return false;
        
        // 反射比较所有字段
        Field[] fieldSrc = clzSrc.getDeclaredFields();
        Field[] fieldDst = clzDst.getDeclaredFields();

        if (fieldSrc.length != fieldDst.length)
            return false;
        
        HashMap map = new HashMap<>(fieldSrc.length);
        // 存储到map，如果成员变量有非基本类型，递归执行
        for (int i = 0; i < fieldSrc.length; i ++) {
            fieldSrc[i].setAccessible(true);
            fieldDst[i].setAccessible(true);

            if (fieldSrc[i].getType() instanceof Integer
                && fieldSrc[i].getType() instanceof Double
                && fieldSrc[i].getType() instanceof Long
                && fieldSrc[i].getType() instanceof Boolean
                && fieldSrc[i].getType() instanceof CharSequence
                && fieldSrc[i].getType() instanceof Float
                && fieldSrc[i].getType() instanceof Byte ) {
                map.put(fieldSrc[i].get(src), map.getOrDefault(fieldSrc[i].get(src), 0) + 1);
                map.put(fieldDst[i].get(dst), map.getOrDefault(fieldDst[i].get(dst), 0) + 1);
             } else {
                return isDeepEquals(fieldSrc[i].get(clzSrc), fieldDst[i].get(clzDst)); // 内部不等，外部也不等，提前结束
             }
            
        }

        int target = 2; // 可以扩展比较多个数
        
        for (Map.Entry<Object, Integer> entry : map.entrySet()) {
            if (entry.value != 2) return false;
        }
        return true;
        
    }
}