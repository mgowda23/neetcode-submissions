class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagram = new HashMap<>();
        for(String i : strs) {
            char[] charArray = i.toCharArray();
            Arrays.sort(charArray);
            String sortedstr = new String(charArray);
            anagram.putIfAbsent(sortedstr, new ArrayList<>());
            anagram.get(sortedstr).add(i);
        }
        return new ArrayList(anagram.values());
    }
}
